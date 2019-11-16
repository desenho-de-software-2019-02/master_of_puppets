#! /bin/bash

echo '======= INSTALLING PKGs'
pip install -r requirements.txt

echo '======= RUNNING SERVER'
python3 app.py
