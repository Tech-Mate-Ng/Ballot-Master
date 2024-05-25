#!/bin/bash

# This script is used to set up a development environment for a project.
# It installs necessary prerequisites, sets up a virtual environment, and creates an .env file for environment variables.

# Update the package list and install prerequisites
echo "Updating package list and installing prerequisites..."
apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	curl

# Install pipx if not already installed
if ! command -v pipx &>/dev/null; then
	echo "Installing pipx..."
	sudo apt update -y
	sudo apt install pipx -y
	pipx ensurepath
	sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
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

# Create a virtual environment called 'bp'
echo "Creating virtual environment..."
python3 -m venv bp

# Activate the virtual environment
echo "Activating virtual environment..."
# shellcheck source=/dev/null
source bp/bin/activate

# Install dependencies using Poetry
echo "Installing dependencies using Poetry..."
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
