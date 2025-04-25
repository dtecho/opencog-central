#!/bin/bash
#
# dependencies.sh - Package dependencies management for ocpkg
#

# Source the utils file for common functions and variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/utils.sh"

# Package definitions
PACKAGES_TOOLS="
    squashfs-tools
    genisoimage
"

PACKAGES_FETCH="
    git
    curl
    wget
"

PACKAGES_ADMIN="
    apt-rdepends
    synaptic
    gdebi
"

# Main build dependencies for Ubuntu 22.04+
PACKAGES_BUILD="
    build-essential
    cmake
    ninja-build
    rlwrap
    binutils-dev
    libiberty-dev
    libltdl-dev
    libicu-dev
    libbz2-dev
    libboost-date-time-dev
    libboost-filesystem-dev
    libboost-math-dev
    libboost-program-options-dev
    libboost-regex-dev
    libboost-serialization-dev
    libboost-thread-dev
    libboost-system-dev
    libboost-random-dev
    libedit-dev
    libpcre2-dev
    libpq-dev
    libtbb-dev
    uuid-dev
    libssl-dev
    libfreetype6-dev
    libatlas-base-dev
    gfortran
    ccache
    cxxtest
    gsasl-common
    libldap2-dev
    krb5-multidev
    libatomic-ops-dev
    libgmp-dev
    libffi-dev
    libreadline-dev
    libunistring-dev
    m4
    autoconf-archive
    autoconf automake autopoint
    libtool
    swig
    flex
    librocksdb-dev
    libopencv-dev
    less
    vim
    libsqlite3-dev
"

# Rust dependencies
PACKAGES_RUST="
    rustc
    cargo
    rust-src
"

PACKAGES_RUNTIME="
    postgresql-client
    netcat-openbsd
"

# Add repositories needed for builds
add_repositories() {
    message "ocpkg" "Adding software repositories..."
    
    # Add any custom repositories if needed
    REPOSITORIES=""
    
    for REPO in $REPOSITORIES; do
        sudo apt-add-repository -y $REPO
    done
    
    sudo apt-get --assume-yes update
    success_message "ocpkg" "Repositories updated successfully"
}

# Install system dependencies
install_dependencies() {
    message "ocpkg" "Installing OpenCog build dependencies..."
    
    # Install the latest python3 version before everything else
    install_python
    
    # Install the main build dependencies
    if ! sudo apt-get --no-upgrade --assume-yes --no-install-recommends install $PACKAGES_BUILD $PACKAGES_RUNTIME $PACKAGES_FETCH liboctomap-dev locales; then
        error_message "ocpkg" "Failed to install dependencies"
        exit 1
    fi
    
    ensure_utf8_installed
    
    # Update ccache links
    update_ccache_links
    
    success_message "ocpkg" "Dependencies installed successfully"
}

# Install Rust dependencies
install_rust_dependencies() {
    message "ocpkg" "Installing Rust dependencies..."
    
    # Check if rustc and cargo are already installed
    if command_exists rustc && command_exists cargo; then
        message "ocpkg" "Rust already installed, updating..."
        rustup update
    else
        message "ocpkg" "Installing Rust..."
        # First try with apt
        if ! sudo apt-get --no-upgrade --assume-yes install $PACKAGES_RUST; then
            # If apt fails, use rustup
            curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
            source "$HOME/.cargo/env"
        fi
    fi
    
    success_message "ocpkg" "Rust dependencies installed successfully"
}

# Install Python and dependencies
install_python() {
    message "ocpkg" "Installing Python..."

    sudo apt-get install -y --no-install-recommends python3-dev
    
    if [[ "$UBUNTU_VERSION" = "\"18.04\"" ]]; then
        sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
        sudo apt-get install -y --no-install-recommends python3-pip
        sudo pip3 install -U pip nose3 cython setuptools
    fi
    if [[ "$UBUNTU_VERSION" = "\"20.04\"" ]]; then
        sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
        sudo apt-get install -y --no-install-recommends python3-nose cython3
    fi
    if [[ "$UBUNTU_VERSION" = "\"22.04\"" ]]; then
        sudo apt-get install -y --no-install-recommends python3-nose cython3
    fi
    
    success_message "ocpkg" "Python installed successfully"
}

# Install pip separately
install_python_pip() {
    message "ocpkg" "Installing Python pip..."
    
    sudo apt-get install -y --no-install-recommends python3-pip
    sudo pip3 install -U pip setuptools
    
    success_message "ocpkg" "Python pip installed successfully"
}

# Install Guile
install_guile() {
    message "ocpkg" "Installing Guile $GUILEVERSION..."
    
    if [[ "$UBUNTU_VERSION" = "\"18.04\"" ]]; then
        sudo apt-get install -y --no-install-recommends guile-2.2-dev
    else
        install_bdwgc
        
        cd /tmp/
        # Clean up remnants from previous install failures, if any
        rm -rf guile-${GUILEVERSION}*
        wget https://ftp.gnu.org/gnu/guile/guile-$GUILEVERSION.tar.gz
        tar -xvf guile-$GUILEVERSION.tar.gz
        cd guile-$GUILEVERSION
        mkdir build
        cd build
        ../configure
        make -j$(nproc)
        sudo make install
        sudo mv /usr/local/lib/libguile-*.so.*-gdb.scm /usr/share/gdb/auto-load/ || true
        sudo ldconfig
        cd /tmp/
        rm -rf guile-${GUILEVERSION}*
    fi
    
    success_message "ocpkg" "Guile $GUILEVERSION installed successfully"
}

# Install BDWGC (Boehm-Demers-Weiser garbage collector)
install_bdwgc() {
    message "ocpkg" "Installing latest bdwgc..."
    
    local _version=$(curl --silent -w %{redirect_url} https://github.com/ivmai/bdwgc/releases/latest \
        | cut -d "\"" -f 2 | cut -d "/" -f 8)
    
    local _dir_name="gc-${_version:1}"
    local _file_name="${_dir_name}.tar.gz"
    local _download_name="${_version}/${_dir_name}.tar.gz"
    
    cd /tmp/
    rm -rf ${_dir_name}*
    
    # Get latest release
    message "ocpkg" "Downloading bdwgc ${_version}..."
    wget https://github.com/ivmai/bdwgc/releases/download/${_download_name}
    
    tar -xvf ${_file_name}
    cd ${_dir_name}
    ./configure --enable-large-config
    make -j$(nproc)
    sudo make install
    sudo ldconfig
    cd /tmp/
    rm -rf ${_dir_name}*
    
    success_message "ocpkg" "BDWGC installed successfully"
}

# Install Haskell dependencies
install_haskell_dependencies() {
    message "ocpkg" "Installing Haskell dependencies in user space..."
    
    sudo wget -qO- https://get.haskellstack.org/ | sh
    
    cd /tmp
    rm -rf patchelf*
    wget "https://nixos.org/releases/patchelf/patchelf-0.9/patchelf-0.9.tar.bz2"
    tar -jxf patchelf-0.9.tar.bz2
    rm patchelf-0.9.tar.bz2
    cd patchelf-0.9
    ./configure
    sudo make install
    cd /tmp
    rm -rf patchelf-0.9
    
    success_message "ocpkg" "Haskell dependencies installed successfully"
}

# Update ccache links
update_ccache_links() {
    message "ocpkg" "Updating ccache links..."
    
    # In Ubuntu some links are absent when build-essential and ccache
    # packages are installed by the same apt-get command
    sudo update-ccache-symlinks
    
    success_message "ocpkg" "ccache links updated successfully"
}

# Ensure UTF-8 locales are installed
ensure_utf8_installed() {
    message "ocpkg" "Ensuring UTF-8 locales are installed..."
    
    if locale -a | grep -q en_US.utf8; then
        message "ocpkg" "UTF-8 locale already enabled"
    else
        sudo sh -c 'echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "ar_AE.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "fa_IR.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "he_IL.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "id_ID.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "kk_KZ.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "lt_LT.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "th_TH.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "tr_TR.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "vi_VN.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "zh_CN.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo sh -c 'echo "zh_HK.UTF-8 UTF-8" >> /etc/locale.gen'
        sudo locale-gen
    fi
    
    success_message "ocpkg" "UTF-8 locales installed successfully"
}