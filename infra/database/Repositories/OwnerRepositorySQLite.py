import sqlite3
from typing import Any

from sqlalchemy import insert
from sqlmodel import Session

from core.entities.repository.owner_repository import OwnerRepository
from core.entities.request.owner import OwnerPost
from infra.database.schema.owner_model import OwnerModel


class OwnerRepositorySQLite(OwnerRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_table(self, engine):
        OwnerModel.metadata.create_all(engine)

    def create(self, schema: OwnerPost) -> Any:
        print("OwnerRepositorySQLite -> create")
        stmt = insert(OwnerModel).values(
            name= schema.name
        )

        self.session.execute(stmt)

