#!/bin/bash

# This script is used to set up a development environment for a project.
# It installs necessary prerequisites, sets up a virtual environment, and creates an .env file for environment variables.

# Add missing import statement for the os module
import os

# Ensure the script is run as a superuser
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root. Please use sudo."
	exit 1
fi

# Update the package list and install prerequisites
echo "Updating package list and installing prerequisites..."
apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	curl

# Install pipx if not already installed
if ! command -v pipx &>/dev/null; then
	echo "Installing pipx..."
	python3 -m pip install --user pipx
	python3 -m pipx ensurepath
	# Add pipx to the current shell session
	export PATH=$PATH:~/.local/bin
fi

# Install Poetry using pipx
if ! command -v poetry &>/dev/null; then
	echo "Installing Poetry..."
	pipx install poetry
fi

# Navigate to the project directory
PROJECT_DIR=$(dirname "$0")
cd "$PROJECT_DIR" || exit

# Set up the virtual environment and install dependencies
echo "Setting up the virtual environment and installing dependencies..."
poetry install

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
	echo "Creating .env file..."
	touch .env
	echo "Please populate the .env file with necessary environment variables."
else
	echo ".env file already exists."
fi

echo "Setup complete. You can now run your application using 'poetry run <command>'."
