"""Módulo de modelos de dados da tabela TODO."""

from common.base_model import AbstractBaseModel
from sqlalchemy.orm import Mapped, mapped_column


class TodoModel(AbstractBaseModel):
    """Representa a tabela Todo no banco de dados."""

    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    task: Mapped[str] = mapped_column(name='str_task_description')
