"""Arquivos utils para aplicação."""
from flask_restful import abort, reqparse

parser = reqparse.RequestParser()
parser.add_argument('task')

def abort_if_todo_doesnt_exist(todo_id: str, todos: dict) -> None:
    """Aborta a requisição se o item TODO não existir."""
    if todo_id not in todos:
        abort(404, message=f"Todo {todo_id} doesn't exist")
