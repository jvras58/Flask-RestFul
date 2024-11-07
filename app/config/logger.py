"""Módulo de configurações de logger."""

import logging
from logging import Logger

from rich.logging import RichHandler


def build_logger(log_level: str, environment: str) -> Logger:
    """Constrói o logger com RichHandler."""
    datefmt_str = (
        '[%X]' if environment == 'development' else '[%Y-%m-%d %X]'
    )
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.DEBUG),
        format='%(message)s',
        datefmt=datefmt_str,
        handlers=[RichHandler()],
    )
    return logging.getLogger()


def get_logger(log_level: str = 'DEBUG', environment: str = 'development') -> Logger:
    """Retorna o logger configurado conforme o nível de log e o ambiente."""
    return build_logger(log_level, environment)
