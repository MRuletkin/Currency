SHELL := /bin/bash

manage_py := python ./app/manage.py

createsuperuser:
	$(manage_py) createsuperuser

run:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

flake8:
	flake8 app/
