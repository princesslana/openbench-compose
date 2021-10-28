#!/bin/bash

set -x
set -e

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=ianagbip1oti@gmail.com

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --no-input || true

python3 manage.py runserver 0.0.0.0:8080
