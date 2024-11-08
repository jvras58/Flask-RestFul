"""Módulo de modelos de dados da tabela TODO."""

from common.base_model import AbstractBaseModel
from config.table_registry import table_registry
from sqlalchemy.orm import Mapped, mapped_column


@table_registry.mapped_as_dataclass
class Todo(AbstractBaseModel):
    """Representa a tabela Todo no banco de dados."""

    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(
        name='id',
        primary_key=True,
        init=False,
        autoincrement=True,
        comment='Identificador da task',
    )
    task: Mapped[str] = mapped_column(name='str_task_description')

    def __init__(self, **kwargs: dict) -> None:
        """Initialize the model."""
        super().__init__(**kwargs)
        for attr, value in kwargs.items():
            setattr(self, attr, value)
