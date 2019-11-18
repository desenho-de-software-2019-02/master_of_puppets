#! /bin/bash

echo '======= INSTALLING PKGs'
pip install -r requirements.txt

echo '======= RUNNING SERVER'
python app.py
