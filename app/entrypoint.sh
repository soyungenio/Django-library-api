#!/bin/bash
while ! (nc -z postgresql-master 5432 && nc -z postgresql-slave 5432)
do
	echo "postgresql-master and postgresql-slave are unavailable - starting"
	sleep 3
done
python manage.py migrate
python manage.py runserver 0.0.0.0:8000