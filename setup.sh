#!/bin/bash

echo "setup virtual environment... \n"
virtualenv env
source env/bin/activate 

echo "installing dependencies...\n"
pip install -r requirements.txt


