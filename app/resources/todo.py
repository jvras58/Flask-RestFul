"""Contém a lógica das rotas para manipulação dos itens TODO."""
from common.utils import abort_if_todo_doesnt_exist, parser

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


class Todo:
    """Lógica de manipulação de um único item TODO."""

    def get(self, todo_id: str) -> dict:
        """Obtém um item TODO."""
        abort_if_todo_doesnt_exist(todo_id, TODOS)
        return TODOS[todo_id]

    def delete(self, todo_id: str) -> dict:
        """Remove um item TODO."""
        abort_if_todo_doesnt_exist(todo_id, TODOS)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id: str) -> dict:
        """Atualiza um item TODO."""
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList:
    """Lógica de manipulação da lista de itens TODO."""

    def get(self) -> dict:
        """Obtém a lista de itens TODO."""
        return TODOS

    def post(self) -> dict:
        """Adiciona um novo item TODO."""
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).replace('todo', '')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
