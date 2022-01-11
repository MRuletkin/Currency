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

collectstatic:
	$(manage_py) collectstatic
shell:
	$(manage_py) shell_plus --print-sql

flake8:
	flake8 app/

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

