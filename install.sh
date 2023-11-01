#!/bin/bash

# Make the Python script executable
chmod +x password_generator.py

# Move the Python script to /usr/local/bin
sudo mv password_generator.py /usr/local/bin/generate_password

echo "Password generator script installed successfully. You can now run 'generate_password' as a command."
