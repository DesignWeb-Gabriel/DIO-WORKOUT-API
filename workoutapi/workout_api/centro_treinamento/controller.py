import uuid
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy import select
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from datetime import datetime
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.dependencies import DatabaseDependency

api_router = APIRouter()

@api_router.post(
    "/", 
    summary="Criar centro de treinamento", 
    status_code=status.HTTP_201_CREATED, 
    response_model=CentroTreinamentoOut
)
async def create_centro_treinamento(db: DatabaseDependency, centro_treinamento_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    centro_id = uuid.uuid4()
    centro_treinamento_model = CentroTreinamentoModel(
        id=centro_id,
        **centro_treinamento_in.model_dump()
    )

    db.add(centro_treinamento_model)
    await db.commit()
    
    return CentroTreinamentoOut(
        id=centro_id,
        **centro_treinamento_in.model_dump()
    )

@api_router.get("/", summary="Listar centros de treinamento",
                status_code=status.HTTP_200_OK,
                response_model=list[CentroTreinamentoOut])
async def get_centro_treinamento(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamento = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return [CentroTreinamentoOut(
        id=centro.id,
        nome=centro.nome,
        endereco=centro.endereco,
        proprietario=centro.proprietario
    ) for centro in centros_treinamento]

@api_router.get("/{centro_treinamento_id}", summary="Buscar centro de treinamento por ID",
                status_code=status.HTTP_200_OK,
                response_model=CentroTreinamentoOut)
async def get_centro_treinamento_by_id(centro_treinamento_id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == centro_treinamento_id))).scalars().first()
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro de treinamento não encontrado")
    return CentroTreinamentoOut(
        id=centro_treinamento.id,
        nome=centro_treinamento.nome,
        endereco=centro_treinamento.endereco,
        proprietario=centro_treinamento.proprietario
    )