"""Representa o modelo base para todos os modelos do aplicativo."""

from dataclasses import dataclass

from sqlalchemy import DateTime, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """Modelo base para todos os modelos do aplicativo."""


@dataclass
class AbstractBaseModel(Base):
    """Modelo base auditável para todos os modelos do aplicativo."""

    __abstract__ = True

    audit_user_login: Mapped[str] = mapped_column(
        String(30),
        name='str_audit_user_login',
        nullable=False,
        comment='Login do usuário que realizou a ação',
    )

    audit_user_ip: Mapped[str] = mapped_column(
        String(16),
        name='str_audit_user_ip',
        nullable=False,
        comment='IP do usuário que realizou a ação',
    )
    audit_created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        name='ts_audit_created_at',
        server_default=func.now(),
        nullable=False,
        init=False,
        comment='Data e hora de criação do registro',
    )
    audit_updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        name='ts_audit_updated_at',
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        init=True,
        comment='Data e hora da última atualização do registro',
    )

    def __init__(self, **kwargs: dict) -> None:
        """Inicialize o modelo."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def get_updated_data(self, obj: 'AbstractBaseModel') -> None:
        """Atualize o modelo com os novos dados."""
        for key, value in obj._as_dict().items():  # noqa: SLF001
            setattr(self, key, value)

    def _as_dict(self, jump_immutable_fields: bool = True) -> dict:
        """Retorne o modelo como um dicionário. Excluindo atributos de auditoria.

        Este método é usado para serializar o modelo e prepará-lo para atualização
        modelo.
        """
        # Esses campos são manipulados pelo banco de dados.
        immutable_fields = ['audit_created_at', 'audit_updated_at']
        return {
            attr.key: getattr(self, attr.key)
            for attr in self.__mapper__.column_attrs
            if jump_immutable_fields and attr.key not in immutable_fields
        }

    def __repr__(self) -> str:
        """Retornar a representação do modelo."""
        return f'<{self.__class__.__name__} {self.id}>'
