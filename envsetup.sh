#!/bin/bash

# This script sets up the environment for a project called 'bp'.
# It installs Poetry, creates a virtual environment, activates it, installs dependencies using Poetry,
# creates a .env file if it doesn't exist, and creates a log file if it doesn't exist.

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
