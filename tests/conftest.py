import pytest
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.session import get_session, Base
from app.startup import app

@pytest.fixture
def client(session):
    """
    Contexto de webclient para teste de APIRest com Flask.

    Returns:
        FlaskClient: Uma instancia de FlaskClient.
    """

    def get_session_override():
        return session

    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()

@pytest.fixture
def session():
    """
    Contexto de Session para teste de estrutura de banco de dados.

    Yields:
        Session: Uma instancia de Session do SQLAlchemy
    """
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
        # echo=True,
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)

@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.

    Args:
        dbapi_connection: O objeto de conexão com o banco de dados.
        connection_record: O objeto de registro de conexão.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()
