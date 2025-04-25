#!/bin/bash
#
# install.sh - Installation of OpenCog components
#

# Source the utils file for common functions and variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/utils.sh"
source "$SCRIPT_DIR/dependencies.sh"

# Install given opencog github repo
install_opencog_github_repo() {
    local REPO="$1"
    message "ocpkg" "Installing ${REPO}..."
    
    cd /tmp/
    # Cleaning up remnants from previous install failures, if any
    rm -rf master.tar.gz* ${REPO}-master
    rm -rf master.tar.gz* ${REPO}-main
    wget "${GITHUB_URL}/${REPO}/archive/master.tar.gz"
    tar -xvf master.tar.gz

    # Newer git repos call them `main` not `master`
    if [ -d ${REPO}-master/ ]; then
        cd ${REPO}-master/
    elif [ -d ${REPO}-main/ ]; then
        cd ${REPO}-main/
    else
        error_message "ocpkg" "Could not find repository directory for ${REPO}"
        return 1
    fi

    # Check if this is a Rust project (has Cargo.toml but no CMakeLists.txt)
    if [ -f "Cargo.toml" ] && [ ! -f "CMakeLists.txt" ]; then
        message "ocpkg" "Building Rust project ${REPO}..."
        cargo build --release
        
        # If there's an install.sh script, run it
        if [ -f "install.sh" ]; then
            chmod +x install.sh
            sudo ./install.sh
        fi
    else
        # Use CMake build process
        message "ocpkg" "Building CMake project ${REPO}..."
        mkdir -p build
        cd build/
        cmake ..
        make -j$(nproc)
        sudo make install
    fi
    
    sudo ldconfig
    cd /tmp/
    rm -rf master.tar.gz ${REPO}-master/
    rm -rf master.tar.gz ${REPO}-main/
    cd $CURRENT_DIR
    
    success_message "ocpkg" "Successfully installed ${REPO}"
}

# Install minicog (minimal installation)
install_minicog() {
    message "ocpkg" "Installing MiniCog (minimal OpenCog installation)..."
    
    # Install dependencies first
    install_dependencies
    install_guile
    
    # Install core components
    for repo in $MINICOG_REPOS; do
        install_opencog_github_repo $repo
    done
    
    success_message "ocpkg" "MiniCog installation complete!"
}

# Install full OpenCog with all repositories
install_full_opencog() {
    message "ocpkg" "Installing Full OpenCog (all repositories)..."
    
    # Install dependencies first
    install_dependencies
    install_guile
    install_rust_dependencies
    
    # Install all repositories in a logical order to handle dependencies
    message "ocpkg" "Installing core components..."
    for repo in $MINICOG_REPOS; do
        install_opencog_github_repo $repo
    done
    
    message "ocpkg" "Installing AtomSpace components..."
    # Install the remaining AtomSpace components (skip those already installed)
    for repo in $ATOMSPACE_REPOS; do
        if ! echo "$MINICOG_REPOS" | grep -q "$repo"; then
            install_opencog_github_repo $repo
        fi
    done
    
    message "ocpkg" "Installing language processing components..."
    for repo in $LANGUAGE_REPOS; do
        install_opencog_github_repo $repo
    done
    
    message "ocpkg" "Installing reasoning components..."
    for repo in $REASONING_REPOS; do
        if ! echo "$MINICOG_REPOS" | grep -q "$repo"; then
            install_opencog_github_repo $repo
        fi
    done
    
    message "ocpkg" "Installing agent components..."
    for repo in $AGENTS_REPOS; do
        install_opencog_github_repo $repo
    done
    
    message "ocpkg" "Installing tools and utilities..."
    for repo in $TOOLS_REPOS; do
        if ! echo "$MINICOG_REPOS" | grep -q "$repo"; then
            install_opencog_github_repo $repo
        fi
    done
    
    message "ocpkg" "Installing UI components..."
    for repo in $UI_REPOS; do
        install_opencog_github_repo $repo
    done
    
    success_message "ocpkg" "Full OpenCog installation complete!"
}

# Install Core AtomSpace
install_atomspace() {
    message "ocpkg" "Installing AtomSpace core components..."
    
    # Install in dependency order
    install_opencog_github_repo atomspace
    install_opencog_github_repo atomspace-rocks
    install_opencog_github_repo atomspace-cog
    install_opencog_github_repo cogserver
    install_opencog_github_repo unify
    
    success_message "ocpkg" "AtomSpace core components installed successfully"
}

# Install Language components
install_language() {
    message "ocpkg" "Installing language components..."
    
    # Install in dependency order
    install_opencog_github_repo lg-atomese
    install_link_grammar
    install_opencog_github_repo learn
    install_opencog_github_repo sensory
    install_opencog_github_repo generate
    install_opencog_github_repo vision
    
    success_message "ocpkg" "Language components installed successfully"
}

# Install all of core OpenCog
install_opencog() {
    message "ocpkg" "Installing OpenCog core components..."
    
    # Install language components first
    install_language
    
    # Install remaining core components
    install_opencog_github_repo ure
    install_opencog_github_repo attention
    install_opencog_github_repo spacetime
    install_opencog_github_repo pln
    install_opencog_github_repo miner
    install_opencog_github_repo asmoses
    install_opencog_github_repo opencog
    install_opencog_github_repo agi-bio
    install_opencog_github_repo benchmark
    
    success_message "ocpkg" "OpenCog core components installed successfully"
}

# Install MOSES
install_moses() {
    message "ocpkg" "Installing MOSES..."
    
    install_opencog_github_repo moses
    
    success_message "ocpkg" "MOSES installed successfully"
}

# Install Link-Grammar
install_link_grammar() {
    message "ocpkg" "Installing Link-Grammar..."
    
    cd /tmp/

    # Cleaning up remnants from previous install failures, if any
    rm -rf link-grammar*
    rm -rf master.tar.gz

    # Get install version from command line
    if [ $# -eq 1 ]; then
        local _version=${1}
        wget https://github.com/opencog/link-grammar/archive/link-grammar-${_version}.tar.gz
        tar -zxf link-grammar-${_version}.tar.gz
        cd link-grammar-link-grammar-${_version}/
    elif [ "$INSTALL_LG_MASTER" == "true" ]; then
        # Master version fails to follow naming convention
        local _version="master"
        wget https://github.com/opencog/link-grammar/archive/master.tar.gz
        tar -zxf master.tar.gz
        cd link-grammar-${_version}/
    else
        # Hunt down the latest tarball version
        local _version=$(git ls-remote -t \
            https://github.com/opencog/link-grammar "link-grammar-5*" \
            | grep -v "\^"| cut -d "-" -f 3 | sort -V | tail -n 1)
        wget https://github.com/opencog/link-grammar/archive/link-grammar-${_version}.tar.gz
        tar -zxf link-grammar-${_version}.tar.gz
        cd link-grammar-link-grammar-${_version}/
    fi
    
    ./autogen.sh --no-configure
    mkdir build
    cd build
    
    if [ "$INSTALL_JAVA_LINK_GRAMMAR" == "true" ]; then
        ../configure
    else
        ../configure --disable-java-bindings
    fi
    
    make -j$(nproc)
    sudo make install
    sudo ldconfig
    
    cd /tmp/
    rm -rf link-grammar*
    rm -rf master.tar.gz
    cd $CURRENT_DIR
    
    success_message "ocpkg" "Link-Grammar installed successfully"
}

# Install notebooks
install_notebooks() {
    message "ocpkg" "Installing notebooks..."

    # Install pip3 and Jupyter notebook
    install_python_pip
    cd
    sudo pip3 install ipython jupyter

    # Installing Guile Kernel
    # Check if site folder exists
    if [ ! -d "/usr/local/share/guile/site" ]; then
        cd /usr/local/share/guile/
        sudo mkdir site
        cd
    fi

    # Install ZeroMQ library
    # Clean up remnants of previous installations
    rm -rf zeromq-4.2.1*
    wget https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz
    tar xvf zeromq-4.2.1.tar.gz
    cd zeromq-4.2.1/
    ./configure
    make
    sudo make install
    cd

    # Install guile-json library
    # Clean up remnants of previous installations
    rm -rf guile-json-0.6.0*
    wget http://download.savannah.gnu.org/releases/guile-json/guile-json-0.6.0.tar.gz
    tar xvf guile-json-0.6.0.tar.gz
    cd guile-json-0.6.0
    ./configure --prefix=/usr/local/
    make
    sudo make install
    cd

    cd `guile -c "(display (%global-site-dir))"`
    # Place guile-simple-zmq library to the guile library folder
    sudo rm -rf simple-zmq.scm*
    sudo wget https://raw.githubusercontent.com/jerry40/guile-simple-zmq/master/src/simple-zmq.scm
    # Edit simple-zmq.scm => set BUF-SIZE to 8192
    sudo sed -i 's/(define BUF-SIZE.*)/(define BUF-SIZE 8192)/' simple-zmq.scm
    cd

    # Kernel setup
    if [ ! -d "/home/$USER/.local/share/jupyter/kernels/guile" ]; then
        sudo mkdir -p /home/$USER/.local/share/jupyter/kernels/guile
    fi

    cd /home/$USER/.local/share/jupyter/kernels/guile
    sudo rm -rf guile-jupyter-kernel.scm hmac.scm kernel.json tools.scm
    sudo wget https://github.com/jerry40/guile-kernel/raw/master/src/guile-jupyter-kernel.scm
    sudo wget https://github.com/jerry40/guile-kernel/raw/master/src/hmac.scm
    sudo wget https://github.com/jerry40/guile-kernel/raw/master/src/kernel.json
    sudo wget https://github.com/jerry40/guile-kernel/raw/master/src/tools.scm
    sudo sed -i 's,\/home.*local,'$HOME/.local',' kernel.json

    echo "export PATH=$PATH:/home/$USER/.local/bin" >> /home/$USER/.bashrc
    echo "source $HOME/.bashrc"
    cd $CURRENT_DIR
    
    success_message "ocpkg" "Notebooks installed successfully"
}

# Function to list all available repositories
list_repositories() {
    message "ocpkg" "Available OpenCog repositories:"
    
    echo -e "\nAtomSpace Components:"
    for repo in $ATOMSPACE_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nLanguage Processing:"
    for repo in $LANGUAGE_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nReasoning Systems:"
    for repo in $REASONING_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nAgents and Bio:"
    for repo in $AGENTS_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nTools and Utilities:"
    for repo in $TOOLS_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nUser Interfaces:"
    for repo in $UI_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nMiniCog Components (minimal installation):"
    for repo in $MINICOG_REPOS; do
        echo "  - $repo"
    done
    
    echo -e "\nUse 'octool -f REPO_NAME' to install a specific repository"
    echo "Use 'octool -M' for MiniCog (minimal installation)"
    echo "Use 'octool -F' for full installation"
}