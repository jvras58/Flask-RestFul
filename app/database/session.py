"""Módulo para gerenciar a sessão do banco de dados."""

from config.settings import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(get_settings().DB_URL)


def get_session() -> Session:
    """Retorna uma sessão do banco de dados."""
    with Session(engine) as session:
        yield session
