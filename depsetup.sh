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
	source ~/.bashrc
fi
