from fastapi import APIRouter, status, Body
from workout_api.atleta.schemas import AtletaIn, AtletaOut
from datetime import datetime

api_router = APIRouter()

@api_router.post("/", summary="Criar atleta", status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def create_atleta(atleta_in: AtletaIn = Body(...)) -> AtletaOut:
    # Por enquanto retornando dados mock - implementar persistência depois
    return AtletaOut(
        pk_id=1,
        nome=atleta_in.nome,
        cpf=atleta_in.cpf,
        idade=atleta_in.idade,
        peso=atleta_in.peso,
        altura=atleta_in.altura,
        sexo=atleta_in.sexo,
        created_at=datetime.now()
    )

@api_router.get("/", summary="Listar atletas")
async def get_atleta():
    return {"message": "Atletas listados com sucesso!"}
