#!/bin/sh

# Install Python dependencies for mkdocs

PYTHON="python" #note, on mac, it may be "python3"
PIP="pip"

main() {
    
    # Chek if python is installed
    if ! command -v $PYTHON &> /dev/null
    then
        echo "Python is not installed"
        exit 1
    fi
    
    # Check if pip is installed
    if ! command -v $PIP &> /dev/null; then
        echo "⚠️ pip not found. Attempting to install..."
        curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        $PYTHON get-pip.py
        rm get-pip.py
    fi
    
    $PIP install "mkdocs<2" mkdocs-material mkdocs-glightbox mkdocs-autorefs mkdocs-literate-nav mike
  
}

main
