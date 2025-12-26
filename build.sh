#!/usr/bin/env bash

set -o errexit

curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64

# Build Tailwind CSS
./tailwindcss-linux-x64 -i ./static/input.css -o ./static/tailwind.css --minify

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python create_superuser.py
