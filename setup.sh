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
	sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
	echo 'export PATH="$PATH:/root/.local/bin"' | sudo tee -a ~/.bashrc
	source ~/.bashrc
fi

# Navigate to the project directory
PROJECT_DIR=$(dirname "$0")
cd "$PROJECT_DIR" || exit

# Install Poetry using pipx
echo "Installing Poetry..."
pipx install poetry

# Create a virtual environment called 'bp'
echo "Creating virtual environment..."
python3 -m venv bp

# Activate the virtual environment
echo "Activating virtual environment..."
# shellcheck source=/dev/null
source bp/bin/activate

# Install Poetry using pipx
echo "Installing Poetry..."
pipx install poetry

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

# Create the log file if it doesn't exist
if [ ! -f log.txt ]; then
	echo "Creating log file..."
	touch log.txt
else
	echo "Log file already exists."
fi

echo "Setup complete. You can now run your application using 'poetry run <command>'."
