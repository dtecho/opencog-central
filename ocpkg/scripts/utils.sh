#!/bin/bash
#
# utils.sh - Common utilities and variables for ocpkg
#

# Set colors for messages
ESC_SEQ="\033["
COL_RESET=$ESC_SEQ"0m"
COL_RED=$ESC_SEQ"31;01m"
COL_GREEN=$ESC_SEQ"32;01m"
COL_YELLOW=$ESC_SEQ"33;01m"
COL_BLUE=$ESC_SEQ"34;01m"

# Common variables
CURRENT_DIR=$(pwd)
PATH_PREFIX=/usr/local
PROCESSORS=$(grep "^processor" /proc/cpuinfo | wc -l)
MAKE_JOBS=${MAKE_JOBS:-$(($PROCESSORS+0))}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GUILEVERSION="3.0.9"
GITHUB_URL="https://github.com/opencog"

# Set paths based on user
if [ "$USER" == "root" ]; then
 HOST_SOURCE_BRANCH=$PATH_PREFIX/src/opencog
 HOST_BUILD_DIR=/tmp/opencog_build
else
 HOST_SOURCE_BRANCH=$CURRENT_DIR/opencog/src
 HOST_BUILD_DIR=$CURRENT_DIR/opencog/build
fi

# Common functions
message() {
    echo -e "\e[1;34m[${1:-ocpkg}] ${2:-$MESSAGE}\e[0m"
}

error_message() {
    echo -e "\e[1;31m[${1:-ocpkg}] ERROR: ${2:-$MESSAGE}\e[0m"
}

success_message() {
    echo -e "\e[1;32m[${1:-ocpkg}] SUCCESS: ${2:-$MESSAGE}\e[0m"
}

# Function to detect the OS and distribution
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$NAME
        OS_VER=$VERSION_ID
        OS_ID=$ID
    else
        OS=$(uname -s)
        OS_VER=$(uname -r)
    fi
    
    echo "Detected OS: $OS $OS_VER ($OS_ID)"
}

# Get distribution version
get_distro_version() {
  cat /etc/os-release | grep "^VERSION_ID="  | cut -d "=" -f 2
}

UBUNTU_VERSION=$(get_distro_version)

# Check if architecture is x86_64
is_x86_64() {
    local ARCH=$(uname -m)
    if [ "$ARCH" == "x86_64" ]; then
        return 0
    else
        return 1
    fi
}

# Check if a command exists
command_exists() {
    command -v "$1" &>/dev/null
}

# Function to check if a directory is inside a git repository
is_git_repo() {
    git -C "$1" rev-parse --is-inside-work-tree &>/dev/null
}

# For shared repository definitions
# Define core repositories for minicog (minimal installation)
MINICOG_REPOS="cogutil atomspace atomspace-rocks cogserver unify ure"

# Define all OpenCog repositories that will be managed
# This is separated by category for better organization
ATOMSPACE_REPOS="
    atomspace 
    atomspace-rocks 
    atomspace-cog 
    cogserver 
    unify 
    atomspace-bridge
    atomspace-dht
    atomspace-ipfs
    atomspace-restful
    atomspace-rpc
    atomspace-websockets
    "

LANGUAGE_REPOS="
    lg-atomese
    link-grammar
    learn
    sensory
    generate
    vision
    language-learning
    "

REASONING_REPOS="
    ure
    pln
    miner
    attention
    spacetime
    "

AGENTS_REPOS="
    agents
    atomspace-agents
    ros-behavior-scripting
    agi-bio
    "

TOOLS_REPOS="
    cogutil
    asmoses
    moses
    opencog
    TinyCog
    benchmark
    pattern-index
    "

UI_REPOS="
    atomspace-explorer
    atomspace-js
    atomspace-typescript
    atomspace-metta
    "

# Combine all repositories for full installation
ALL_REPOS="$ATOMSPACE_REPOS $LANGUAGE_REPOS $REASONING_REPOS $AGENTS_REPOS $TOOLS_REPOS $UI_REPOS"

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