SHELL := /bin/bash

manage_py := docker exec -it backend python ./app/manage.py


run:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

flake8:
	docker exec -it backend flake8 app/

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker exec -it backend bash -c "pytest ./app/tests --cov=app --cov-report html"

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

collectstatic:
	$(manage_py) collectstatic --noinput && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

