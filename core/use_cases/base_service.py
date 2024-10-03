from typing import Any, Protocol

class BaseService(Protocol):
    def handle(self, *args, **kwargs) -> Any: ...