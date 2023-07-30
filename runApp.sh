#!/bin/bash

# check if Python virtual environment env exists
if [ ! -f "venv/bin/activate" ]; then
    ./install.sh
    exit 1
fi

# activate Python virtual environment
source venv/bin/activate

# run the test suite
./runTests.sh

python app.py