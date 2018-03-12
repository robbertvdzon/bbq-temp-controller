#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /home/pi/git/bbq-temp-controller
git pull
python Smoker.py
