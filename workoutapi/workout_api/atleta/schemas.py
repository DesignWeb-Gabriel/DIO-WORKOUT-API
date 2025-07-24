from typing import Annotated, Optional
from datetime import datetime
from pydantic import Field, PositiveFloat, UUID4
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaOut
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="João da Silva", min_length=3, max_length=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678901", min_length=11, max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25, min_value=18, max_value=100)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=70.5, min_value=30, max_value=200)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75, min_value=1.5, max_value=2.5)]
    sexo: Annotated[str, Field(description="Gênero do atleta", example="M", min_length=1, max_length=1)]
    
class AtletaIn(Atleta):
    categoria: Annotated[str, Field(description="Nome da categoria do atleta")]
    centro_treinamento: Annotated[str, Field(description="Nome do centro de treinamento do atleta")]

class AtletaOut(Atleta, OutMixin):
    id: Annotated[UUID4, Field(description="ID do atleta")]
    categoria: Annotated[CategoriaOut, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoOut, Field(description="Centro de treinamento do atleta")]

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta", example="João da Silva", min_length=3, max_length=100)]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta", example=25, min_value=18, max_value=100)]
    peso: Annotated[Optional[PositiveFloat], Field(None, description="Peso do atleta", example=70.5, min_value=30, max_value=200)]
    altura: Annotated[Optional[PositiveFloat], Field(None, description="Altura do atleta", example=1.75, min_value=1.5, max_value=2.5)]
    