"""Módulo de modelos de dados para o Swagger."""
from config.config import api
from flask_restx import fields

todo_model = api.model('Todo', {
    'task': fields.String(required=True, description='Descrição da tarefa'),
})
