#!/bin/bash
echo  starting server
exec gunicorn incrideaadmin.wsgi:application --bind 0:5000