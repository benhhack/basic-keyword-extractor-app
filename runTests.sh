#!/bin/bash

# activate the virtual environment
. ./venv/bin/activate

# run the test suite
python -m pytest --webdriver Firefox app/test_app_vis.py

# collect exit code from pytest
# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi