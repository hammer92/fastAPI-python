from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from core.entities.request.owner import OwnerPost, OwnerResponse
from core.use_cases.owner_cases.owner_create_service import OwnerCreateService
from infra.database.Repositories.OwnerRepositorySQLite import OwnerRepositorySQLite
from infra.database.session_db import SessionDB

OwnerRouter = APIRouter(prefix="/v1/owners", tags=["owner"])

def get_owner_create_service():
    return OwnerCreateService(repository=OwnerRepositorySQLite(session=SessionDB))

@OwnerRouter.post(
    "/",
    response_model=OwnerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    owner: OwnerPost,
    owner_service: Annotated[
        OwnerCreateService,
        Depends(get_owner_create_service)]
):
    return owner_service.handle(owner=owner)