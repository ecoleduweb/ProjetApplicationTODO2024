#!/bin/bash

# Update package list and upgrade existing packages
sudo apt-get update
sudo apt-get upgrade -y

# Install Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
sudo apt install nodejs -y

source ~/.nvm/nvm.sh

nvm install v20.11.0

# Install Python 3.12
sudo apt install -y python3.12

echo "Installation complete."
