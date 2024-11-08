"""Módulo de modelos de dados da tabela TODO."""

from common.base_model import AbstractBaseModel
from config.table_registry import table_registry
from sqlalchemy.orm import Mapped, mapped_column


@table_registry.mapped_as_dataclass
class TodoModel(AbstractBaseModel):
    """Representa a tabela Todo no banco de dados."""

    __tablename__ = 'todo'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    task: Mapped[str] = mapped_column(name='str_task_description')

    def __init__(self, **kwargs: dict) -> None:
        """Initialize the model."""
        super().__init__(**kwargs)
        for attr, value in kwargs.items():
            setattr(self, attr, value)
