from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import URL
from sqlmodel import Session, create_engine

from core.entities.config import get_environment_variables
from infra.database.Repositories.OwnerRepositorySQLite import OwnerRepositorySQLite

settings = get_environment_variables()


url = URL.create(
    drivername=settings.DATABASE_DIALECT,  # driver name = postgresql + the library we are using
    username=settings.DATABASE_USERNAME,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOSTNAME,
    database=settings.DATABASE_NAME,
    port=settings.DATABASE_PORT
)
engine = create_engine(url, echo=True)



def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDB = Annotated[Session, Depends(get_db)]