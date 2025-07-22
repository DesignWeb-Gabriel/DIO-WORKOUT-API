from typing import Annotated
from datetime import datetime
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema, OutMixin


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", min_length=3, max_length=10)]


class CategoriaOut(CategoriaIn, OutMixin):
    pk_id: Annotated[int, Field(description="ID da categoria", example=1)]
    created_at: Annotated[datetime, Field(description="Data de criação da categoria")]