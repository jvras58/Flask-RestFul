"""Documentação do Swagger."""


def init_swagger() -> object:
    """Inicializa o Swagger."""
    from flask_restx import Api
    from app.resources.todo_router import todo_bp

    return Api(
        todo_bp,
        doc='/docs',
        title='TODO API',
        description='API para gerenciar TODOs',
    )
