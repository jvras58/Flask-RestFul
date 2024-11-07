"""Modulo que define o Blueprint para o resources `TODO` e configura o Swagger para as rotas."""

from flask import Blueprint
from flask_restx import Api, Resource, fields
from .todo import Todo, TodoList


todo_bp = Blueprint('todos', __name__, url_prefix='/todos')
api = Api(todo_bp, doc='/docs', title="TODO API", description="API para gerenciar TODOs")


todo_model = api.model('Todo', {
    'task': fields.String(required=True, description='Descrição da tarefa')
})

todo_ns = api.namespace('', description='Operações relacionadas aos TODOs')

todo_logic = Todo()
todo_list_logic = TodoList()

@todo_ns.route('/')
class TodoListResource(Resource):
    """Operações relacionadas a criação e listagem de TODOs"""
    @api.marshal_list_with(todo_model)
    def get(self):
        """Obtém a lista de TODOs"""
        return todo_list_logic.get()

    @api.expect(todo_model)
    @api.marshal_with(todo_model, code=201)
    def post(self):
        """Cria um novo TODO"""
        return todo_list_logic.post()

@todo_ns.route('/<string:todo_id>')
class TodoResource(Resource):
    """Operações relacionadas a um TODO específico"""
    @api.marshal_with(todo_model)
    def get(self, todo_id):
        """Obtém um TODO específico"""
        return todo_logic.get(todo_id)

    def delete(self, todo_id):
        """Remove um TODO"""
        return todo_logic.delete(todo_id)

    @api.expect(todo_model)
    @api.marshal_with(todo_model)
    def put(self, todo_id):
        """Atualiza um TODO"""
        return todo_logic.put(todo_id)

api.add_namespace(todo_ns)
