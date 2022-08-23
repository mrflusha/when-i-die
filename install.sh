#!/bin/bash
mkdir project-vk-when-i-die
cd when project-vk-when-i-die
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
python3 –m pip install beautifulsoup4 pipreqs requests pymysql
touch parse .py
subl .
