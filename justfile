MANAGE := "python manage.py"

default:
	@just -l

install:
	uv pip install -r requirements.txt 

prepare:
	{{MANAGE}} migrate

run:
	{{MANAGE}} runserver

