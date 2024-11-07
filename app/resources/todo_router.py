"""Modulo que define o Blueprint para o resources `TODO` e configura o Swagger para as rotas."""

from config.config import api
from flask_restx import Resource
from swagger import todo_model

from .todo import Todo, TodoList

todo_ns = api.namespace('tasks', path='', description='Operações relacionadas aos TODOs')

todo_logic = Todo()
todo_list_logic = TodoList()

@todo_ns.route('/', methods=['GET', 'POST'])
class TodoListResource(Resource):
    """Operações relacionadas a criação e listagem de TODOs."""

    def get(self) -> list:
        """Obtém a lista de TODOs."""
        return todo_list_logic.get()

    @api.expect(todo_model)
    @api.marshal_with(todo_model, code=201)
    def post(self) -> dict:
        """Cria um novo TODO."""
        return todo_list_logic.post()

@todo_ns.route('/<string:todo_id>', methods=['GET', 'DELETE','PUT'])
class TodoResource(Resource):
    """Operações relacionadas a um TODO específico."""

    @api.marshal_with(todo_model)
    def get(self, todo_id: str) -> dict:
        """Obtém um TODO específico."""
        return todo_logic.get(todo_id)

    def delete(self, todo_id: str) -> dict:
        """Remove um TODO."""
        return todo_logic.delete(todo_id)

    @api.expect(todo_model)
    @api.marshal_with(todo_model)
    def put(self, todo_id: str) -> dict:
        """Atualiza um TODO."""
        return todo_logic.put(todo_id)
