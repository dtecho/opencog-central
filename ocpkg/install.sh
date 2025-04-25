#!/bin/bash
# ocpkg installation script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Installing ocpkg from $SCRIPT_DIR..."

# Step 1: Update the bash script to make it ready
echo "Setting up bash script version..."
sudo chmod +x "$SCRIPT_DIR/ocpkg"
sudo ln -sf "$SCRIPT_DIR/ocpkg" /usr/local/bin/octool

# Step 2: Build the Rust version
echo "Building Rust version of ocpkg..."
cd "$SCRIPT_DIR"
cargo build --release

# Step 3: Install the Rust binary
echo "Installing Rust binary..."
sudo ln -sf "$SCRIPT_DIR/target/release/ocpkg" /usr/local/bin/ocpkg

# Step 4: Install dependencies needed by ocpkg
echo "Installing required dependencies..."
octool -r -d -R

echo "ocpkg has been installed successfully!"
echo "You can use 'ocpkg' for the Rust version or 'octool' for the bash version."
echo "Try 'ocpkg help' for more information."