#!/bin/bash
#
# main.sh - Main entry point for the ocpkg tool
#

# Source the utils and other module scripts
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/utils.sh"
source "$SCRIPT_DIR/dependencies.sh"
source "$SCRIPT_DIR/install.sh"
source "$SCRIPT_DIR/build.sh"

# Default settings
DEFAULT_PACKAGE_TYPE=local
DEFAULT_ADD_REPOSITORIES=true
DEFAULT_INSTALL_DEPENDENCIES=true
DEFAULT_UPDATE_OPENCOG=true
DEFAULT_BUILD_OPENCOG=false
DEFAULT_TEST_OPENCOG=false

# Package type descriptions
declare -A PACKAGE_DESCRIPTION=(
  [local]="Local install with no packaging (default)"
  [demo]="LiveCD ISO image ~700MB with OpenCog Demo (auto-starting)"
  [min]="LiveCD ISO image ~700MB with OpenCog Server"
  [dev]="LiveDVD ISO image ~900MB with OpenCog Development Environment"
  [kvm]="TBD Ubuntu KVM image with OpenCog Server"
  [demovm]="TBD Ubuntu VirtualBox image with OpenCog Unity3D proxy for demo"
  [debs]="TBD Ubuntu packages (deb files)"
  [docker]="TBD Docker Images"
  [minicog]="Minimal compact OpenCog installation with core components only"
  [full]="Full OpenCog installation with all components"
)

# Display usage information
usage() {
    if [ "$SELF_NAME" == "$TOOL_NAME" ]; then
        echo "Usage: $SELF_NAME OPTION"
        echo " -r Add software repositories"
        echo " -d Install base/system build dependencies"
        echo " -p Install python build dependencies"
        echo " -s Install haskell build dependencies in user space. Don't use sudo"
        echo " -i Install build-job artifacts"
        echo " -c Install CogUtil"
        echo " -a Install AtomSpace"
        echo " -f Install from opencog github repo. Pass the name of the repo as an argument"
        echo " -o Install OpenCog"
        echo " -n Install notebook"
        echo " -l [master|java] Install Link Grammar release tarball; else master branch"
        echo " -m Install MOSES"
        echo " -z Install the language subsystem"
        echo " -g Install Guile $GUILEVERSION"
        echo " -b Build source code in git worktree found @ $PWD"
        echo " -e Build examples in git worktree found @ $PWD"
        echo " -t Run tests of source code in git worktree found @ $PWD"
        echo " -j [jobs] override number of auto-detected make jobs"
        echo " -w Download data for the opencog repo"
        echo " -v Verbose output for 'apt-get' commands"
        echo " -R Install Rust dependencies"
        echo " -M Install MiniCog (minimal compact installation)"
        echo " -F Install Full OpenCog (all repositories)"
        echo " -L List all available repositories"
        echo " -h This help message"
    else
        echo "Usage: $SELF_NAME [OPTIONS] [PACKAGE-TYPE]"
        echo "  PACKAGE-TYPES:"
        for key in ${!PACKAGE_DESCRIPTION[@]}; do
            echo "   " ${key} $'\t' "${PACKAGE_DESCRIPTION[$key]}"
        done
        echo "    (Live CD: Ubuntu ISO image ~700MB will be downloaded if none found.)"
        echo "  OPTIONS:"
        echo "    -i [filename]  ISO input filename"
        echo "    -o [filename]  ISO output filename"
        echo "    -j [jobs]      override number of auto-detected make jobs"
        echo "    -n             suppress git updates"
    fi
}

# Process command line options
process_options() {
    # Determine how the script was called
    SELF_NAME=$(basename "$0")
    TOOL_NAME=octool
    NO_ARGS=false
    
    if [ $# -eq 0 ]; then 
        NO_ARGS=true
    fi

    if [ "$SELF_NAME" == "$TOOL_NAME" ]; then
        while getopts "abdef:gipcrstl:mhvj:ownzRMFL" flag; do
            case $flag in
                r) ADD_REPOSITORIES=true ;;
                d) INSTALL_DEPENDENCIES=true ;; # base development packages
                w) DOWNLOAD_DATA=true ;;
                p) INSTALL_OPENCOG_PYTHON_PACKAGES=true ;;
                c) INSTALL_COGUTIL=true ;;
                a) INSTALL_ATOMSPACE=true ;;
                f) INSTALL_FROM_REPO="$OPTARG" ;;
                o) INSTALL_OPENCOG=true ;;
                l) INSTALL_LINK_GRAMMAR=true ;
                    if [ "$OPTARG" == "master" ]; then
                        INSTALL_LG_MASTER=true
                    elif [ "$OPTARG" == "java" ]; then
                        INSTALL_JAVA_LINK_GRAMMAR=true
                    fi ;;
                m) INSTALL_MOSES=true ;;
                n) INSTALL_NOTEBOOKS=true ;;
                g) INSTALL_GUILE=true ;;
                b) BUILD_SOURCE=true ;;
                e) BUILD_EXAMPLES=true ;;
                t) TEST_SOURCE=true ;;
                v) unset QUIET ;;
                z) INSTALL_LANGUAGE=true ;;
                j) MAKE_JOBS="$OPTARG" ;;
                s) HASKELL_STACK_SETUP=true ;;
                i) INSTALL_BUILD=true ;;
                R) INSTALL_RUST_DEPS=true ;;
                M) INSTALL_MINICOG=true ;;
                F) INSTALL_FULL=true ;;
                L) LIST_REPOS=true ;;
                h) usage ; exit 0 ;;
                \?) usage; exit 1 ;;
                *) UNKNOWN_FLAGS=true ;;
            esac
        done
    else
        while getopts ":i:o:j:s:c:l:r:adubtnxrvh" flag; do
            case $flag in
                i) INPUT_ISO_NAME="$OPTARG" ;;
                o) OUTPUT_ISO_NAME="$OPTARG" ;;
                j) MAKE_JOBS="$OPTARG" ;; # override auto-detected MAKE_JOBS
                s) HOST_SOURCE_BRANCH="$OPTARG" ;;
                c) HOST_BUILD_DIR="$OPTARG" ;; # local cached build dir
                l) LIVE_BUILD_DIR="$OPTARG" ;; # live build directory
                r) BZR_REVISION="$OPTARG" ;;
                a) ADD_REPOSITORIES=true ;;
                d) INSTALL_DEPENDENCIES=true ;; # ALL, none
                u) UPDATE_OPENCOG=true ;; # git pull
                b) BUILD_OPENCOG=true ;; # build opencog
                t) TEST_OPENCOG=true ;; # test opencog
                n) unset DEFAULT_UPDATE_OPENCOG ;; # suppress git update
                x) unset DEFAULT_BUILD_OPENCOG ;; # suppress build
                p) REINSTALL_PACKAGES=true ;;
                v) unset QUIET ;;
                h) usage ; exit 0 ;;
                \?) usage ; exit 1 ;;
                *) UNKNOWN_FLAGS=true ;;
            esac
        done
    fi

    shift $((OPTIND-1))

    # Handle direct package type selection
    PACKAGE_TYPE=$DEFAULT_PACKAGE_TYPE

    if [ $1 ] && [ "$SELF_NAME" != "$TOOL_NAME" ]; then
        case $1 in
            debs)    PACKAGE_TYPE=$1 ;;
            dev)     PACKAGE_TYPE=$1 ;;
            demo)    PACKAGE_TYPE=$1 ;;
            kvm)     PACKAGE_TYPE=$1 ;;
            min)     PACKAGE_TYPE=$1 ;;
            local)   PACKAGE_TYPE=$1 ;;
            docker)  PACKAGE_TYPE=$1 ;;
            minicog) PACKAGE_TYPE=$1 ;;
            full)    PACKAGE_TYPE=$1 ;;
            *)       MESSAGE="Package type not recognized."; message "ocpkg" "$MESSAGE"; usage; exit 1 ;;
        esac
        MESSAGE="Package type: $PACKAGE_TYPE : ${PACKAGE_DESCRIPTION[$PACKAGE_TYPE]}"
        message "ocpkg" "$MESSAGE"
    fi
    
    return 0
}

# Main execution function
main() {
    # Process command line options
    process_options "$@"
    
    # Check for unknown flags or no arguments
    if [ "$UNKNOWN_FLAGS" = true ]; then usage; exit 1; fi
    if [ "$NO_ARGS" = true ]; then usage; exit 1; fi

    # Execute based on flags when run as octool
    if [ "$SELF_NAME" == "$TOOL_NAME" ]; then
        if [ "$LIST_REPOS" = true ]; then list_repositories; exit 0; fi
        if [ "$ADD_REPOSITORIES" = true ]; then add_repositories; fi
        if [ "$INSTALL_DEPENDENCIES" = true ]; then install_dependencies; fi
        if [ "$DOWNLOAD_DATA" = true ]; then download_data; fi
        if [ "$HASKELL_STACK_SETUP" = true ]; then install_haskell_dependencies; fi
        if [ "$INSTALL_OPENCOG_PYTHON_PACKAGES" = true ]; then install_opencog_python_packages; fi
        if [ "$INSTALL_COGUTIL" = true ]; then install_cogutil; fi
        if [ "$INSTALL_ATOMSPACE" = true ]; then install_atomspace; fi
        if [ "$INSTALL_LANGUAGE" = true ]; then install_language; fi
        if [ "$INSTALL_FROM_REPO" ]; then install_opencog_github_repo "$INSTALL_FROM_REPO"; fi
        if [ "$INSTALL_NOTEBOOKS" = true ]; then install_notebooks; fi
        if [ "$INSTALL_OPENCOG" = true ]; then install_opencog; fi
        if [ "$INSTALL_LINK_GRAMMAR" = true ]; then install_link_grammar; fi
        if [ "$INSTALL_MOSES" = true ]; then install_moses; fi
        if [ "$INSTALL_GUILE" = true ]; then install_guile; fi
        if [ "$BUILD_SOURCE" = true ]; then build_source; fi
        if [ "$BUILD_EXAMPLES" = true ]; then build_examples; fi
        if [ "$TEST_SOURCE" = true ]; then test_source; fi
        if [ "$INSTALL_BUILD" = true ]; then install_build; fi
        if [ "$INSTALL_RUST_DEPS" = true ]; then install_rust_dependencies; fi
        if [ "$INSTALL_MINICOG" = true ]; then install_minicog; fi
        if [ "$INSTALL_FULL" = true ]; then install_full_opencog; fi
        
        exit 0
    fi

    # Set default option values when not specified
    if [ -z "$ADD_REPOSITORIES" ]; then ADD_REPOSITORIES=$DEFAULT_ADD_REPOSITORIES; fi
    if [ -z "$INSTALL_DEPENDENCIES" ]; then INSTALL_DEPENDENCIES=$DEFAULT_INSTALL_DEPENDENCIES; fi
    if [ -z "$UPDATE_OPENCOG" ]; then UPDATE_OPENCOG=$DEFAULT_UPDATE_OPENCOG; fi
    if [ -z "$BUILD_OPENCOG" ]; then BUILD_OPENCOG=$DEFAULT_BUILD_OPENCOG; fi
    if [ -z "$TEST_OPENCOG" ]; then TEST_OPENCOG=$DEFAULT_TEST_OPENCOG; fi

    # Handle package type for ocpkg
    case $PACKAGE_TYPE in
        minicog) add_repositories; install_minicog ;;
        full) add_repositories; install_full_opencog ;;
        local) 
            if [ "$ADD_REPOSITORIES" = true ]; then add_repositories; fi
            if [ "$INSTALL_DEPENDENCIES" = true ]; then install_dependencies; fi
            if [ "$UPDATE_OPENCOG" = true ]; then update_opencog_source; fi
            if [ "$BUILD_OPENCOG" = true ]; then build_source; fi
            ;;
        demo|min|dev)
            MESSAGE="Package type '$PACKAGE_TYPE' is not yet implemented in the modular version"
            error_message "ocpkg" "$MESSAGE"
            exit 1
            ;;
        *)
            MESSAGE="Unknown package type: $PACKAGE_TYPE"
            error_message "ocpkg" "$MESSAGE"
            exit 1
            ;;
    esac
}

# Call the main function with all arguments
main "$@"