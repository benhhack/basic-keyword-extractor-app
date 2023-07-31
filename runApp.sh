#!/bin/bash

# check if Python virtual environment env exists
if [ ! -f "venv/bin/activate" ]; then
    ./create.sh
    exit 1
fi

# activate Python virtual environment
source venv/bin/activate

# install the relevant packages
echo "Install packages in requirements.txt"
pip install --upgrade pip
pip install -r requirements.txt

# run the test suite
#./runTests.sh

python app/app.py