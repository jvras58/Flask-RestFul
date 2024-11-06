SHEll := /bin/zsh
.PHONY: venv

venv:
	@poetry run poetry install

commit:
	@echo "Revisar mudanças para este commit: "
	@echo "-------------------------------------"
	@git status -s 
	@echo "-------------------------------------"
	@read -p "Commit msg: " menssagem ; \
	git add . ;\
	git commit -m "$$menssagem" ;\

update:
	@git fetch origin
	@git pull
	@$(MAKE) venv

lint:
	task lint \
	task format

dev:
	export FLASK_APP=app/startup.py && export FLASK_ENV=development && flask run --debug

prod:
	export FLASK_APP=app/startup.py && export FLASK_ENV=production && flask run
