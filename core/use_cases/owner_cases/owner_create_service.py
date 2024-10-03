from typing import Any

from core.entities.repository.owner_repository import OwnerRepository
from core.entities.request.owner import OwnerResponse, OwnerPost
from core.use_cases.base_service import BaseService


class OwnerCreateService(BaseService):

    def __init__(self, repository: OwnerRepository):
        self._repository = repository

    def handle(self, owner:OwnerPost, *args, **kwargs) -> OwnerResponse | None:
        print("OwnerCreateService -> handle")
        self._repository.create(schema = owner)
        return OwnerResponse(**owner.dict())
