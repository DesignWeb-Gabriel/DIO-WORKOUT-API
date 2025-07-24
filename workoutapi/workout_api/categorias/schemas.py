from typing import Annotated
from datetime import datetime
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema, OutMixin


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", min_length=3, max_length=100)]


class CategoriaOut(CategoriaIn, OutMixin):
    id: Annotated[UUID4, Field(description="ID da categoria")]