#!/bin/bash
cd ~
cd pgAdmin4
virtualenv pgAdmin4
cd pgAdmin4
source bin/activate
xdg-open http://localhost:5050
python lib/python3.8/site-packages/pgadmin4/pgAdmin4.py
