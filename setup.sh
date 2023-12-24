#!/bin/bash
read -p 'Enter the path to your project: ' project_path
# Create the virtual environment
python3 -m venv "$project_path/venv"

# Activate the virtual environment
source "$project_path/venv/bin/activate"

# Install pipreqs
pip install pipreqs

# Generate requirements.txt
pipreqs "$project_path"

# Install requirements
pip install -r "$project_path/requirements.txt"

echo "Requirements installed successfully."