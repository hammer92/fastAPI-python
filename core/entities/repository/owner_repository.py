from typing import Any, Protocol

from core.entities.request.owner import OwnerPost


class OwnerRepository(Protocol):
    def create(self, schema: OwnerPost) -> Any:
        pass

