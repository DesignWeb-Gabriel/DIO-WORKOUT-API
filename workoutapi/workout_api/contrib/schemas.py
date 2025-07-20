from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime


class BaseSchema(BaseModel):
  class Config:
    extra = "forbid"
    from_attributes = True

class OutMixin(BaseSchema):
  pk_id: Annotated[int, Field(description="ID do registro", example=1)]
  created_at: Annotated[datetime, Field(description="Data de criação do registro", example=datetime.now())]
  updated_at: Annotated[datetime, Field(description="Data de atualização do registro", example=datetime.now())]
