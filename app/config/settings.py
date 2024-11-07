"""Módulo de configurações."""

import logging
from functools import lru_cache
from logging import Logger

from pydantic_settings import BaseSettings, SettingsConfigDict
from rich.logging import RichHandler


class Settings(BaseSettings):
    """Classe que representa as configurações setadas no .env da aplicação."""

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encode='utf-8',
        secrets_dir='.secrets',
    )

    DB_URL: str


def build_logger(log_level: str, environment: str) -> Logger:
    """Constrói o logger com RichHandler."""
    datefmt_str = '[%X]' if environment == 'development' else '[%Y-%m-%d %X]'
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.DEBUG),
        format='%(message)s',
        datefmt=datefmt_str,
        handlers=[RichHandler()],
    )
    return logging.getLogger()


def get_logger(
    log_level: str = 'DEBUG',
    environment: str = 'development',
) -> Logger:
    """Retorna o logger configurado conforme o nível de log e o ambiente."""
    return build_logger(log_level, environment)


@lru_cache
def get_settings() -> Settings:
    """Retorna as configurações setadas no .env."""
    return Settings()
