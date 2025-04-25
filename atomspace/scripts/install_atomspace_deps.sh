#!/bin/bash
# install_atomspace_deps.sh
# Script to download and install prerequisites for OpenCog AtomSpace
# This script installs both required and optional dependencies with a focus on
# language bindings (Python, Haskell, OCaml) and storage backends

set -e  # Exit on error
set -u  # Treat unset variables as errors

# Default download directory for source files
SOURCE_DIR="${SOURCE_DIR:-$HOME/atomspace_deps_source}"
# Flag to force source download even if packages are already installed
FORCE_DOWNLOAD="${FORCE_DOWNLOAD:-false}"

show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Install AtomSpace prerequisites and optionally download source files."
    echo ""
    echo "Options:"
    echo "  --download-only     Only download source files without installing packages"
    echo "  --force-download    Force download even if packages are already installed"
    echo "  --source-dir DIR    Directory to store downloaded source files (default: $SOURCE_DIR)"
    echo "  --with-postgres     Include PostgreSQL dependencies"
    echo "  --with-python       Include Python bindings dependencies (default: yes)"
    echo "  --with-haskell      Include Haskell bindings dependencies"
    echo "  --with-ocaml        Include OCaml bindings dependencies"
    echo "  --help              Display this help message and exit"
    echo ""
}

# Parse command-line options
DOWNLOAD_ONLY=false
WITH_POSTGRES=false
WITH_PYTHON=true
WITH_HASKELL=false
WITH_OCAML=false

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
        --with-postgres)
            WITH_POSTGRES=true
            shift
            ;;
        --with-python)
            WITH_PYTHON=true
            shift
            ;;
        --without-python)
            WITH_PYTHON=false
            shift
            ;;
        --with-haskell)
            WITH_HASKELL=true
            shift
            ;;
        --with-ocaml)
            WITH_OCAML=true
            shift
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

echo "Installing AtomSpace prerequisites..."
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

# Function to download Boost source
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

# Function to download CMake source
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

# Function to download Guile source
download_guile() {
    echo "Downloading Guile source..."
    GUILE_VERSION="3.0.9"
    
    cd "$SOURCE_DIR"
    if [ ! -f "guile-${GUILE_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        wget -c "https://ftp.gnu.org/gnu/guile/guile-${GUILE_VERSION}.tar.gz"
    else
        echo "Guile source already downloaded. Skipping."
    fi
}

# Function to download CxxTest source
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

# Function to download Python and Cython sources
download_python_deps() {
    if [ "$WITH_PYTHON" = true ]; then
        echo "Downloading Python dependencies..."
        
        # Download Python
        PYTHON_VERSION="3.10.8"
        cd "$SOURCE_DIR"
        if [ ! -f "Python-${PYTHON_VERSION}.tar.xz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz"
        else
            echo "Python source already downloaded. Skipping."
        fi
        
        # Download Cython
        CYTHON_VERSION="0.29.32"
        if [ ! -f "Cython-${CYTHON_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://github.com/cython/cython/archive/refs/tags/${CYTHON_VERSION}.tar.gz" -O "Cython-${CYTHON_VERSION}.tar.gz"
        else
            echo "Cython source already downloaded. Skipping."
        fi
    fi
}

# Function to download Haskell sources (GHC and cabal)
download_haskell_deps() {
    if [ "$WITH_HASKELL" = true ]; then
        echo "Downloading Haskell dependencies..."
        
        # Download GHC
        GHC_VERSION="9.2.5"
        cd "$SOURCE_DIR"
        if [ ! -f "ghc-${GHC_VERSION}-src.tar.xz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://downloads.haskell.org/~ghc/${GHC_VERSION}/ghc-${GHC_VERSION}-src.tar.xz"
        else
            echo "GHC source already downloaded. Skipping."
        fi
        
        # Download cabal
        CABAL_VERSION="3.6.2.0"
        if [ ! -f "cabal-install-${CABAL_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://github.com/haskell/cabal/archive/refs/tags/cabal-install-v${CABAL_VERSION}.tar.gz" -O "cabal-install-${CABAL_VERSION}.tar.gz"
        else
            echo "Cabal source already downloaded. Skipping."
        fi
    fi
}

# Function to download OCaml sources
download_ocaml_deps() {
    if [ "$WITH_OCAML" = true ]; then
        echo "Downloading OCaml dependencies..."
        
        # Download OCaml
        OCAML_VERSION="4.14.0"
        cd "$SOURCE_DIR"
        if [ ! -f "ocaml-${OCAML_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://github.com/ocaml/ocaml/archive/refs/tags/${OCAML_VERSION}.tar.gz" -O "ocaml-${OCAML_VERSION}.tar.gz"
        else
            echo "OCaml source already downloaded. Skipping."
        fi
        
        # Download findlib
        FINDLIB_VERSION="1.9.5"
        if [ ! -f "findlib-${FINDLIB_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "http://download.camlcity.org/download/findlib-${FINDLIB_VERSION}.tar.gz"
        else
            echo "FindLib source already downloaded. Skipping."
        fi
    fi
}

# Function to download PostgreSQL sources
download_postgres_deps() {
    if [ "$WITH_POSTGRES" = true ]; then
        echo "Downloading PostgreSQL dependencies..."
        
        # Download PostgreSQL
        POSTGRES_VERSION="14.3"
        cd "$SOURCE_DIR"
        if [ ! -f "postgresql-${POSTGRES_VERSION}.tar.gz" ] || [ "$FORCE_DOWNLOAD" = true ]; then
            wget -c "https://ftp.postgresql.org/pub/source/v${POSTGRES_VERSION}/postgresql-${POSTGRES_VERSION}.tar.gz"
        else
            echo "PostgreSQL source already downloaded. Skipping."
        fi
    fi
}

# Function to download cogutil sources
download_cogutil() {
    echo "Downloading cogutil source..."
    cd "$SOURCE_DIR"
    if [ ! -d "cogutil" ] || [ "$FORCE_DOWNLOAD" = true ]; then
        if [ -d "cogutil" ]; then
            rm -rf "cogutil"
        fi
        git clone https://github.com/opencog/cogutil.git
    else
        echo "cogutil git repository already cloned. Skipping."
    fi
}

# Function to download all source files
download_all_sources() {
    echo "Downloading all dependency sources as fallback..."
    download_boost
    download_cmake
    download_guile
    download_cxxtest
    download_cogutil
    
    # Optional dependencies
    download_python_deps
    download_haskell_deps
    download_ocaml_deps
    download_postgres_deps
    
    echo "All source packages downloaded to $SOURCE_DIR"
    echo "You can use these source packages to build dependencies if package installation fails"
}

# Function to install dependencies on Debian-based systems
install_debian_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping package installation"
        return
    fi
    
    echo "Detected Debian/Ubuntu-based system. Installing dependencies..."
    
    # Update package lists
    sudo apt-get update
    
    # Install build tools
    sudo apt-get install -y build-essential cmake

    # Install required dependencies
    sudo apt-get install -y \
        libboost-dev \
        libboost-date-time-dev \
        libboost-filesystem-dev \
        libboost-program-options-dev \
        libboost-regex-dev \
        libboost-serialization-dev \
        libboost-system-dev \
        libboost-thread-dev \
        guile-3.0-dev \
        cxxtest
    
    # Install Python bindings dependencies
    if [ "$WITH_PYTHON" = true ]; then
        echo "Installing Python binding dependencies..."
        sudo apt-get install -y \
            python3-dev \
            python3-pip \
            cython3
        sudo pip3 install pytest
    fi
    
    # Install Haskell binding dependencies
    if [ "$WITH_HASKELL" = true ]; then
        echo "Installing Haskell binding dependencies..."
        sudo apt-get install -y \
            ghc \
            cabal-install \
            libghc-text-dev \
            libghc-network-dev \
            libghc-hourglass-dev
    fi
    
    # Install OCaml binding dependencies
    if [ "$WITH_OCAML" = true ]; then
        echo "Installing OCaml binding dependencies..."
        sudo apt-get install -y \
            ocaml \
            ocaml-findlib \
            libfindlib-ocaml-dev
    fi
    
    # Install PostgreSQL dependencies
    if [ "$WITH_POSTGRES" = true ]; then
        echo "Installing PostgreSQL dependencies..."
        sudo apt-get install -y \
            postgresql \
            postgresql-client \
            libpq-dev
    fi
    
    echo "All Debian/Ubuntu dependencies installed successfully!"
}

# Function to install dependencies on RHEL-based systems
install_rhel_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping package installation"
        return
    fi
    
    echo "Detected CentOS/RHEL-based system. Installing dependencies..."
    
    # Install build tools
    sudo yum install -y gcc gcc-c++ make cmake

    # Install EPEL repository for additional packages
    sudo yum install -y epel-release
    
    # Install required dependencies
    sudo yum install -y \
        boost-devel \
        guile-devel \
        cxxtest
    
    # Install Python bindings dependencies
    if [ "$WITH_PYTHON" = true ]; then
        echo "Installing Python binding dependencies..."
        sudo yum install -y \
            python3-devel \
            python3-pip \
            python3-Cython
        sudo pip3 install pytest
    fi
    
    # Install Haskell binding dependencies
    if [ "$WITH_HASKELL" = true ]; then
        echo "Installing Haskell binding dependencies..."
        sudo yum install -y \
            ghc \
            cabal-install
    fi
    
    # Install OCaml binding dependencies
    if [ "$WITH_OCAML" = true ]; then
        echo "Installing OCaml binding dependencies..."
        sudo yum install -y \
            ocaml \
            ocaml-findlib
    fi
    
    # Install PostgreSQL dependencies
    if [ "$WITH_POSTGRES" = true ]; then
        echo "Installing PostgreSQL dependencies..."
        sudo yum install -y \
            postgresql \
            postgresql-server \
            postgresql-devel
    fi
    
    echo "All CentOS/RHEL dependencies installed successfully!"
}

# Function to install dependencies from source (if needed)
install_source_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping source installation"
        return
    fi
    
    echo "Installing some dependencies from source..."
    
    # Create a temporary directory for source installation
    TEMP_DIR=$(mktemp -d)
    
    # Install CxxTest from source if not already installed
    if ! command -v cxxtestgen &> /dev/null; then
        echo "Installing CxxTest from source..."
        
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
    
    # Install cogutil from source
    echo "Installing cogutil from source..."
    if [ -d "$SOURCE_DIR/cogutil" ]; then
        cp -r "$SOURCE_DIR/cogutil" "$TEMP_DIR/"
    else
        cd "$TEMP_DIR"
        git clone https://github.com/opencog/cogutil.git
    fi
    
    cd "$TEMP_DIR/cogutil"
    mkdir -p build
    cd build
    cmake ..
    make -j$(nproc)
    sudo make install
    
    # Clean up temporary directory
    rm -rf "$TEMP_DIR"
    
    echo "Source dependencies installed successfully!"
}

# Function to install Rust dependencies (since we're in a Rust development container)
install_rust_deps() {
    if [ "$DOWNLOAD_ONLY" = true ]; then
        echo "Download-only mode enabled, skipping Rust dependencies installation"
        return
    fi
    
    echo "Installing Rust dependencies for AtomSpace..."
    
    # Make sure Rust is up to date
    rustup update
    
    # Install common Rust utilities that might be used with AtomSpace
    cargo install cargo-edit cargo-expand cargo-watch
    
    echo "Rust dependencies installed successfully!"
}

# Function to run tests for Python bindings
run_python_tests() {
    if [ "$DOWNLOAD_ONLY" = true ] || [ "$WITH_PYTHON" = false ]; then
        return
    fi
    
    echo "Running Python binding tests..."
    # These tests would normally be run after building the AtomSpace
    echo "Note: Python binding tests should be run after building the AtomSpace with:"
    echo "  cd build && make test_python"
    echo "This will verify that the Python bindings are working correctly."
}

# Main execution
download_all_sources

if [ "$DOWNLOAD_ONLY" = false ]; then
    # Install appropriate dependencies based on detected distribution
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

    # Install Rust dependencies
    install_rust_deps
    
    # Install some dependencies from source
    install_source_deps
    
    # Run Python binding tests if requested
    run_python_tests

    echo ""
    echo "AtomSpace prerequisites installation completed successfully!"
    echo "You can now build AtomSpace by running:"
    echo "    mkdir build"
    echo "    cd build"
    echo "    cmake .."
    echo "    make -j$(nproc)"
    echo "    sudo make install"
    echo ""
    echo "To run tests:"
    echo "    make -j$(nproc) check"
else
    echo ""
    echo "Source download completed successfully!"
    echo "All dependency source files have been downloaded to: $SOURCE_DIR"
fi