"""Exemplo de aplicação RESTful com Flask."""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Dicionário para armazenar os itens TODO.
# $ make init
todos = {}


class TodoSimple(Resource):
    """Classe que implementa um recurso RESTful para manipular um único item TODO."""

    def get(self, todo_id: str) -> dict:
        """Obtém um item TODO."""
        if todo_id not in todos:
            return {todo_id: 'Not found'}, 404
        return {todo_id: todos[todo_id]}

    def put(self, todo_id: str) -> dict:
        """Atualiza um item TODO."""
        if request.form['data']:
            todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run()
