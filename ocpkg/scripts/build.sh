#!/bin/bash
#
# build.sh - Build and test functionality for OpenCog components
#

# Source the utils file for common functions and variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/utils.sh"

# Set source and build directories for a project
set_source_and_build_dir() {
    if git rev-parse --is-inside-work-tree 2>/dev/null; then
        SOURCE_DIR=$(git rev-parse --show-toplevel)
        message "ocpkg" "Source Directory is set to $SOURCE_DIR"
        
        if [ -d "$SOURCE_DIR/build" ]; then
            BUILD_DIR="$SOURCE_DIR/build"
            message "ocpkg" "Build Directory is set to $SOURCE_DIR/build"
        else
            mkdir -p "$SOURCE_DIR/build"
            BUILD_DIR="$SOURCE_DIR/build"
            message "ocpkg" "Created Build Directory at $SOURCE_DIR/build"
        fi
        return 0
    else
        error_message "ocpkg" "Not inside a git repository. Please run from within a git repository."
        return 1
    fi
}

# Build function for opencog, atomspace, moses & cogutil repos
build_source() {
    if ! set_source_and_build_dir; then
        return 1
    fi
    
    # Remove CMake cache if it exists to ensure a clean build
    if [ -f "$BUILD_DIR/CMakeCache.txt" ]; then
        rm "$BUILD_DIR/CMakeCache.txt"
        message "ocpkg" "Removed cmake cache file: $BUILD_DIR/CMakeCache.txt"
    fi
    
    message "ocpkg" "Configuring build with CMake..."
    cmake -B"$BUILD_DIR" -H"$SOURCE_DIR"
    
    message "ocpkg" "Building source with $MAKE_JOBS parallel jobs..."
    make -C "$BUILD_DIR" -j$MAKE_JOBS
    
    success_message "ocpkg" "Successfully built source code"
    return 0
}

# Build examples function
build_examples() {
    if ! set_source_and_build_dir; then
        return 1
    fi
    
    # Remove CMake cache if it exists
    if [ -f "$BUILD_DIR/CMakeCache.txt" ]; then
        rm "$BUILD_DIR/CMakeCache.txt"
        message "ocpkg" "Removed cmake cache file: $BUILD_DIR/CMakeCache.txt"
    fi
    
    message "ocpkg" "Configuring build with CMake..."
    cmake -B"$BUILD_DIR" -H"$SOURCE_DIR"
    
    message "ocpkg" "Building examples with $MAKE_JOBS parallel jobs..."
    make -C "$BUILD_DIR" -j$MAKE_JOBS examples
    
    success_message "ocpkg" "Successfully built examples"
    return 0
}

# Run tests function
test_source() {
    if ! set_source_and_build_dir; then
        return 1
    fi
    
    # Remove CMake cache if it exists
    if [ -f "$BUILD_DIR/CMakeCache.txt" ]; then
        rm "$BUILD_DIR/CMakeCache.txt"
        message "ocpkg" "Removed cmake cache file: $BUILD_DIR/CMakeCache.txt"
    fi
    
    message "ocpkg" "Configuring build with CMake..."
    cmake -B"$BUILD_DIR" -H"$SOURCE_DIR"
    
    message "ocpkg" "Building and running tests with $MAKE_JOBS parallel jobs..."
    make -C "$BUILD_DIR" -j$MAKE_JOBS test
    
    success_message "ocpkg" "Successfully ran all tests"
    return 0
}

# Install build job artifacts
install_build() {
    if ! set_source_and_build_dir; then
        return 1
    fi
    
    message "ocpkg" "Starting installation of build artifacts..."
    cd "$BUILD_DIR"
    sudo make install
    sudo ldconfig
    cd "$CURRENT_DIR"
    
    success_message "ocpkg" "Successfully installed build artifacts"
    return 0
}

# Download data needed for examples and tests
download_data() {
    DOWNLOAD_DIR="$HOME/.opencog/data"
    message "ocpkg" "Downloading OpenCog's datasets to $DOWNLOAD_DIR..."
    
    if [ ! -d "$DOWNLOAD_DIR" ]; then
        mkdir -p "$DOWNLOAD_DIR"
    fi

    # Download example datasets
    if [ ! -f "$DOWNLOAD_DIR/gtwc-en-333333-words.scm" ]; then
        wget -O "$DOWNLOAD_DIR/gtwc-en-333333-words.scm" \
            https://raw.githubusercontent.com/opencog/test-datasets/master/concept_nodes/gtwc-en-333333-words.scm
    fi
    
    success_message "ocpkg" "Successfully downloaded required datasets"
}

# Update source code repositories
update_opencog_source() {
    if [ -d "$SOURCE_DIR/.git" ]; then
        message "ocpkg" "Updating OpenCog source at $SOURCE_DIR..."
        cd "$SOURCE_DIR"
        git pull
        cd -
        success_message "ocpkg" "Source code updated successfully"
    else
        error_message "ocpkg" "No git repository found at $SOURCE_DIR"
        return 1
    fi
}