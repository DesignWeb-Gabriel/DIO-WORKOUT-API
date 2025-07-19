from pydantic import BaseModel

class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", example="João da Silva", min_length=3, max_length=100)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678901", min_length=11, max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25, min_value=18, max_value=100)]
    peso: Annotated[Positivefloat, Field(description="Peso do atleta", example=70.5, min_value=30, max_value=200)]
    altura: Annotated[Positivefloat, Field(description="Altura do atleta", example=1.75, min_value=1.5, max_value=2.5)]
    sexo: Annotated[str, Field(description="Gênero do atleta", example="M", min_length=1, max_length=1)]
    objetivo: Annotated[str, Field(description="Objetivo do atleta", example="Perder peso", min_length=1, max_length=100)]
