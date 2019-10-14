#! /bin/bash

echo '======= CHECKING FOR UNINSTALLED PKGs AND INSTALLING'
pip freeze || pip install -r requirements.txt

echo '======= RUNNING SERVER'
python app.py
