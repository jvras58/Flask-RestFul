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

playground:
	@poetry run python src/playground.py

init:
	@echo "Populando todos: "
	curl -X PUT -d "data=Remember the milk" http://localhost:5000/todo1
	@echo "-------------------------------------"
	curl -X PUT -d "data=Change my brakepads" http://localhost:5000/todo2
	@echo "-------------------------------------"
	@echo "Listando todos: "
	@echo "-------------------------------------"
	curl -X GET http://localhost:5000/todo1
	@echo "-------------------------------------"
	curl -X GET http://localhost:5000/todo2
	@echo "-------------------------------------"
