"""Modulo base para configuração da aplicação."""

from config.settings import get_logger, log_response
from database.session import engine
from database.migrate import migrate
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS
from resources.todo_router import todo_bp

def create_app(**config: str) -> Flask:
    """Configuração do CORS e carregamento das extensões."""
    app = Flask(__name__)

    FlaskDynaconf(app, settings_files=["settings.toml"])
    app.config.update(config)

    CORS(app)

    migrate.init_app(app, engine, render_as_batch=True)

    logger = get_logger(app.config['LOG_LEVEL'], app.config['ENVIRONMENT'])
    for rule in app.url_map.iter_rules():
        logger.info("Rota: %s -> Endpoint: %s", rule, rule.endpoint)
    logger.info("Ambiente atual: %s", app.config['ENVIRONMENT'])
    logger.info("Aplicação inicializada com sucesso!")

    app.after_request(log_response)

    app.register_blueprint(todo_bp)

    return app
