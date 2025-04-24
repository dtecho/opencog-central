FROM opencog/opencog-dev:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install additional dev tools
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-tk \
    vim \
    nano \
    git \
    curl \
    wget \
    build-essential \
    cmake \
    ccache \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Set up non-root user for VS Code
ARG USERNAME=opencog
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Check if the user exists, if not create it
RUN if ! id -u $USERNAME > /dev/null 2>&1; then \
        groupadd --gid $USER_GID $USERNAME && \
        useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
        echo "$USERNAME:$USERNAME" | chpasswd && \
        usermod -aG sudo $USERNAME && \
        echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
    fi

# Set up proper permissions for user
RUN mkdir -p /home/$USERNAME/.ccache \
    && chown -R $USERNAME:$USERNAME /home/$USERNAME \
    && chown -R $USERNAME:$USERNAME /workspaces 2>/dev/null || true

# Set up Rust for opencog user
USER $USERNAME
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/home/$USERNAME/.cargo/bin:${PATH}"

# Switch back to root for final steps
USER root

# Install Python dependencies
COPY requirements.txt* /tmp/requirements.txt
RUN if [ -f "/tmp/requirements.txt" ]; then \
        pip3 install --no-cache-dir -r /tmp/requirements.txt; \
    fi

# Set working directory
WORKDIR /workspaces/opencog-central

# Reset back to opencog user for VS Code
USER $USERNAME
