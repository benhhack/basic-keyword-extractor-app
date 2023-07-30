rm -rf env/

echo "Creating Python virtual environment env"
python -m venv env/
source env/bin/activate

echo "Install packages in requirements.txt"
pip install --upgrade pip
pip install -r requirements.txt
deactivate