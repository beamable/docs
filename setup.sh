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
    
    # Install from the pinned requirements.txt rather than resolving names
    # here. Direct dependencies are mkdocs, mkdocs-material, mkdocs-glightbox,
    # mkdocs-autorefs, mkdocs-literate-nav, mike, mkdocs-swagger-ui-tag, and
    # mkdocs-open-in-new-tab;
    # requirements.txt pins those plus their whole transitive tree. See the
    # header of that file for why, and for how to regenerate it.
    REQUIREMENTS="$(dirname "$0")/requirements.txt"

    if [ ! -f "$REQUIREMENTS" ]; then
        echo "requirements.txt not found next to setup.sh at $REQUIREMENTS"
        echo "It lives on the main branch; run setup.sh from a main checkout."
        exit 1
    fi

    $PIP install -r "$REQUIREMENTS"

}

main
