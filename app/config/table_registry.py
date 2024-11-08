import threading

from sqlalchemy.orm import registry


class TableRegistry:
    """Singleton para garantir uma única instância de registry."""

    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if (
                    cls._instance is None
                ):  # Verificação dupla para evitar race conditions
                    cls._instance = registry()
        return cls._instance


# Obtendo a instância única de table_registry
table_registry = TableRegistry.get_instance()
