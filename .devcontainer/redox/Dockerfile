# Use an official Rust image as the base
FROM rust:latest

# Updated April 24, 2025 - Install necessary dependencies with correct package names
RUN apt-get update && \
    apt-get install -y qemu-system qemu-system-x86 build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Clone the Redox OS repository
RUN git clone https://gitlab.redox-os.org/redox-os/redox.git /redox
WORKDIR /redox

# Don't try to build Redox OS during container creation as it requires additional setup
# The build will be triggered by the user when needed

# Default command to run Redox with QEMU when manually invoked
CMD ["bash"]
