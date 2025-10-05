#!/bin/bash
# Run migrations and start server
python manage.py migrate
python manage.py runserver 0.0.0.0:8090
