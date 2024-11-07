"""Módulo de configuração do Flask."""

from common.utils import todo_bp
from flask_restx import Api

api = Api(
    todo_bp,
    doc='/docs',
    title="TODO API",
    description="API para gerenciar TODOs",
)
