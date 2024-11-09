"""Módulo para gerenciar a sessão do banco de dados."""

from config.settings import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(get_settings().DB_URL)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def get_session() -> scoped_session:
    """Retorna uma sessão do banco de dados."""
    session = Session()
    try:
        yield session
    finally:
        session.close()
