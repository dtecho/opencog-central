#!/bin/bash
# install_cogutil_deps.sh
# Script to download and install prerequisites for OpenCog Utilities (cogutil)
# This script installs both required and optional dependencies
# With added functionality to download source archives as fallback

set -e  # Exit on error
set -u  # Treat unset variables as errors

# Default download directory for source files
SOURCE_DIR="${SOURCE_DIR:-$HOME/opencog_deps_source}"
# Flag to force source download even if packages are already installed
FORCE_DOWNLOAD="${FORCE_DOWNLOAD:-false}"

show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Install cogutil prerequisites and optionally download source files."
    echo ""
    echo "Options:"
    echo "  --download-only     Only download source files without installing packages"
    echo "  --force-download    Force download even if packages are already installed"
    echo "  --source-dir DIR    Directory to store downloaded source files (default: $SOURCE_DIR)"
    echo "  --help              Display this help message and exit"
    echo ""
}

# Parse command-line options
DOWNLOAD_ONLY=false
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --download-only)
            DOWNLOAD_ONLY=true
            shift
            ;;
        --force-download)
            FORCE_DOWNLOAD=true
            shift
            ;;
        --source-dir)
            SOURCE_DIR="$2"
            shift 2
            ;;
        --help)
            show_usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

echo "Installing cogutil prerequisites..."
if [ "$DOWNLOAD_ONLY" = false ]; then
    echo "This script requires sudo privileges to install packages."
fi
echo "Source files will be downloaded to: $SOURCE_DIR"

# Create source directory if it doesn't exist
mkdir -p "$SOURCE_DIR"

# Detect the Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
    DISTRO_VERSION=$VERSION_ID
else
    echo "Cannot detect Linux distribution. This script supports Ubuntu/Debian and CentOS/RHEL systems."
    exit 1
fi

download_boost() {
    echo "Downloading Boost source..."
    BOOST_VERSION="1.78.0"
    BOOST_FILENAME="boost_${BOOST_VERSION//./_}"
    
    cd "$SOURCE_DIR"
    if [ ! -f "${BOOST_FILENAME}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/${BOOST_FILENAME}.tar.gz"
    else
        echo "Boost source already downloaded. Skipping."
    fi
}

download_cmake() {
    echo "Downloading CMake source..."
    CMAKE_VERSION="3.23.1"
    
    cd "$SOURCE_DIR"
    if [ ! -f "cmake-${CMAKE_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz"
    else
        echo "CMake source already downloaded. Skipping."
    fi
}

download_cxxtest() {
    echo "Downloading CxxTest source..."
    CXXTEST_VERSION="4.4"
    
    cd "$SOURCE_DIR"
    if [ ! -f "cxxtest-${CXXTEST_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://github.com/CxxTest/cxxtest/releases/download/${CXXTEST_VERSION}/cxxtest-${CXXTEST_VERSION}.tar.gz"
    else
        echo "CxxTest source already downloaded. Skipping."
    fi
    
    # Also clone the repository for the latest version
    if [ ! -d "cxxtest-git" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        if [ -d "cxxtest-git" ]; then
            rm -rf "cxxtest-git"
        fi
        git clone https://github.com/CxxTest/cxxtest.git cxxtest-git
    else
        echo "CxxTest git repository already cloned. Skipping."
    fi
}

download_binutils() {
    echo "Downloading binutils source..."
    BINUTILS_VERSION="2.38"
    
    cd "$SOURCE_DIR"
    if [ ! -f "binutils-${BINUTILS_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://ftp.gnu.org/gnu/binutils/binutils-${BINUTILS_VERSION}.tar.gz"
    else
        echo "Binutils source already downloaded. Skipping."
    fi
}

download_doxygen() {
    echo "Downloading Doxygen source..."
    DOXYGEN_VERSION="1.9.4"
    
    cd "$SOURCE_DIR"
    if [ ! -f "doxygen-${DOXYGEN_VERSION}.src.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://www.doxygen.nl/files/doxygen-${DOXYGEN_VERSION}.src.tar.gz"
    else
        echo "Doxygen source already downloaded. Skipping."
    fi
}

download_all_sources() {
    echo "Downloading all dependency sources as fallback..."
    download_boost
    download_cmake
    download_cxxtest
    download_binutils
    download_doxygen
    
    echo "All source packages downloaded to $SOURCE_DIR"
    echo "You can use these source packages to build dependencies if package installation fails"
}

install_debian_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping package installation"
        return
    fi
    
    echo "Detected Debian/Ubuntu-based system. Installing dependencies..."
    
    # Update package lists
    sudo apt-get update
    
    # Install required dependencies
    sudo apt-get install -y \
        build-essential \
        cmake \
        cxxtest \
        libboost-dev \
        libboost-filesystem-dev \
        libboost-program-options-dev \
        libboost-system-dev \
        libboost-thread-dev
    
    # Install optional dependencies (recommended for OpenCog development)
    sudo apt-get install -y \
        binutils-dev \
        libiberty-dev \
        doxygen
    
    echo "All Debian/Ubuntu dependencies installed successfully!"
}

install_rhel_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping package installation"
        return
    fi
    
    echo "Detected CentOS/RHEL-based system. Installing dependencies..."
    
    # Install required dependencies
    sudo yum install -y \
        gcc-c++ \
        make \
        cmake \
        boost-devel \
        cxxtest
    
    # Install optional dependencies
    sudo yum install -y \
        binutils-devel \
        doxygen

    echo "Note: libiberty might be part of gcc-c++ or binutils on RHEL systems."
    echo "All CentOS/RHEL dependencies installed successfully!"
}

install_source_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping source installation"
        return
    fi
    
    echo "Installing some dependencies from source..."
    
    # Create a temporary directory for source installation
    TEMP_DIR=$(mktemp -d)
    
    # Install cxxtest from source if not already installed
    if ! command -v cxxtestgen &> /dev/null; then
        echo "Installing cxxtest from source..."
        
        # Check if we have downloaded the source already
        if [ -d "$SOURCE_DIR/cxxtest-git" ]; then
            cp -r "$SOURCE_DIR/cxxtest-git" "$TEMP_DIR/cxxtest"
        else
            cd "$TEMP_DIR"
            git clone https://github.com/CxxTest/cxxtest.git
        fi
        
        cd "$TEMP_DIR/cxxtest"
        sudo cp -r cxxtest /usr/local/include/
        sudo cp -r bin/* /usr/local/bin/
    fi

    # Clean up temporary directory
    rm -rf "$TEMP_DIR"
    
    echo "Source dependencies installed successfully!"
}

# Main execution
download_all_sources

if [ "$DOWNLOAD_ONLY" = false ]; then
    case $DISTRO in
        ubuntu|debian|linuxmint)
            install_debian_deps
            ;;
        centos|rhel|fedora|rocky|almalinux)
            install_rhel_deps
            ;;
        *)
            echo "Unsupported distribution: $DISTRO"
            echo "This script supports Ubuntu/Debian and CentOS/RHEL systems."
            echo "Source files have been downloaded and can be built manually."
            exit 1
            ;;
    esac

    # Install additional dependencies from source
    install_source_deps

    echo ""
    echo "Cogutil prerequisites installation completed successfully!"
    echo "You can now build cogutil by running:"
    echo "    mkdir build"
    echo "    cd build"
    echo "    cmake .."
    echo "    make"
    echo "    sudo make install"
else
    echo ""
    echo "Source download completed successfully!"
    echo "All dependency source files have been downloaded to: $SOURCE_DIR"
fi