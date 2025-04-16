#!/bin/sh

# Install Python dependencies for mkdocs

main() {
    
    # Chek if python is installed
    if ! command -v python &> /dev/null
    then
        echo "Python is not installed"
        exit 1
    fi
    
    # Check if pip is installed
    if ! command -v pip &> /dev/null; then
        echo "⚠️ pip not found. Attempting to install..."
        curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py
        rm get-pip.py
    fi
    
    pip install mkdocs-material mkdocs-glightbox mkdocs-autorefs mike
  
}

main
