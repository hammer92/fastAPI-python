from datetime import datetime

from pydantic import BaseModel

class OwnerPost(BaseModel):
    name:str
    last_name:str
    id_card:int
    phone:int
    date_of_birth:datetime
    email:str
    password:str

class OwnerResponse(BaseModel):
    name:str
    last_name:str
    id_card:int
    phone:int
    date_of_birth:datetime
    email:str