from fastapi import APIRouter, status
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.atleta.schemas import AtletaIn
from fastapi import Body
 

api_router = APIRouter()

@api_router.post("/atleta",summary="Criar atleta", status_code=status.HTTP_201_CREATED)
async def create_atleta(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    return {"message": "Atleta criado com sucesso!"}

@api_router.get("/atleta",summary="Listar atletas")
async def get_atleta():
    return {"message": "Hello, World!"}
