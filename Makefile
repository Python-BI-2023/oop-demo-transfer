# Styles
isort:
	isort .

black:
	black .

fix-style: isort black

isort-check:
	isort --check-only --diff .

flake8-check:
	flake8 .

check-style: isort-check flake8-check

# RUN
start-script:
	python3 main.py

start-db:
	docker-compose up -d

run: start-db start-script

