#!/bin/bash
python3 sales/manage.py migrate --noinput
python3 sales/manage.py collectstatic --noinput

exec "$@"