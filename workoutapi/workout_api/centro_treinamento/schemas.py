from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
  nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Centro de treinamento 1", min_length=3, max_length=50)]
  endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua das Flores, 123", min_length=10, max_length=100)]
  proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", example="João da Silva", min_length=3, max_length=100)]

class CentroTreinamentoOut(CentroTreinamentoIn): 
  id: Annotated[UUID4, Field(description="ID do centro de treinamento")]