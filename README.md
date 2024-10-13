

# Redux OS Machine Learning Integration Environment

This repository contains the necessary files to set up a machine learning integration environment using Redux OS for the development of an AGI OS with OpenCog Hyperon. The environment supports various programming languages such as Python, Rust, Prolog, and C.

## Setup

To set up the environment, follow these steps:

1. Clone this repository onto your local machine.
2. Install Docker if you do not already have it installed.
3. Open the `devcontainer.json` file located in the `.devcontainer` folder.
4. Configure any specific properties for VS Code, such as settings and extensions.
5. Run the `postCreateCommand` to install the necessary requirements for the environment.
6. Build the Docker image using the `Dockerfile` located in the `.devcontainer` folder.

## Running the App

To run the app, follow these steps:

1. Open the `app.py` file located in the root directory.
2. Make sure you have the necessary programming languages and libraries installed.
3. Run the file using the `launch.json` configuration located in the `.vscode` folder.

## Additional Notes

- The `requirements.txt` file contains the necessary libraries for the app to run.
- The `launch.json` file is configured to run the `app.py` file using the Python interpreter.
- The `Dockerfile` installs the necessary programming languages and libraries for the environment.
- The `devcontainer.json` file allows for customization of the VS Code environment within the Docker container.
