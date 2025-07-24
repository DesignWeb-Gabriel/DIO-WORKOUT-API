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
async def create_centro_treinamento(db_session: DatabaseDependency, centro_treinamento_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    # Verificar se centro de treinamento já existe
    centro_exists = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_in.nome)
    )).scalars().first()
    
    if centro_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Já existe um centro de treinamento com o nome: {centro_treinamento_in.nome}'
        )
    
    try:
        centro_id = uuid.uuid4()
        centro_treinamento_model = CentroTreinamentoModel(
            id=centro_id,
            nome=centro_treinamento_in.nome,
            endereco=centro_treinamento_in.endereco,
            proprietario=centro_treinamento_in.proprietario,
            created_at=datetime.utcnow()
        )

        db_session.add(centro_treinamento_model)
        await db_session.commit()
        await db_session.refresh(centro_treinamento_model)
        
        return CentroTreinamentoOut(
            id=centro_treinamento_model.id,
            nome=centro_treinamento_model.nome,
            endereco=centro_treinamento_model.endereco,
            proprietario=centro_treinamento_model.proprietario,
            created_at=centro_treinamento_model.created_at,
            updated_at=centro_treinamento_model.updated_at
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao criar o centro de treinamento'
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
        proprietario=centro.proprietario,
        created_at=centro.created_at,
        updated_at=centro.updated_at
    ) for centro in centros_treinamento]

@api_router.get("/{centro_treinamento_id}", summary="Buscar centro de treinamento por ID",
                status_code=status.HTTP_200_OK,
                response_model=CentroTreinamentoOut)
async def get_centro_treinamento_by_id(centro_treinamento_id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == centro_treinamento_id)
    )).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Centro de treinamento não encontrado"
        )
    
    return CentroTreinamentoOut(
        id=centro_treinamento.id,
        nome=centro_treinamento.nome,
        endereco=centro_treinamento.endereco,
        proprietario=centro_treinamento.proprietario,
        created_at=centro_treinamento.created_at,
        updated_at=centro_treinamento.updated_at
    )

@api_router.patch("/{centro_treinamento_id}", summary="Atualizar centro de treinamento",
                 status_code=status.HTTP_200_OK,
                 response_model=CentroTreinamentoOut)
async def update_centro_treinamento(centro_treinamento_id: UUID4, db_session: DatabaseDependency, centro_treinamento_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == centro_treinamento_id)
    )).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de treinamento não encontrado"
        )
    
    # Verificar se novo nome já existe em outro centro
    if centro_treinamento_in.nome != centro_treinamento.nome:
        nome_exists = (await db_session.execute(
            select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_in.nome)
        )).scalars().first()
        
        if nome_exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Já existe um centro de treinamento com o nome: {centro_treinamento_in.nome}'
            )
    
    try:
        centro_treinamento.nome = centro_treinamento_in.nome
        centro_treinamento.endereco = centro_treinamento_in.endereco
        centro_treinamento.proprietario = centro_treinamento_in.proprietario
        
        await db_session.commit()
        await db_session.refresh(centro_treinamento)
        
        return CentroTreinamentoOut(
            id=centro_treinamento.id,
            nome=centro_treinamento.nome,
            endereco=centro_treinamento.endereco,
            proprietario=centro_treinamento.proprietario,
            created_at=centro_treinamento.created_at,
            updated_at=centro_treinamento.updated_at
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao atualizar o centro de treinamento'
        )

@api_router.delete("/{centro_treinamento_id}", summary="Deletar centro de treinamento",
                  status_code=status.HTTP_204_NO_CONTENT)
async def delete_centro_treinamento(centro_treinamento_id: UUID4, db_session: DatabaseDependency) -> None:
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).where(CentroTreinamentoModel.id == centro_treinamento_id)
    )).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de treinamento não encontrado"
        )
    
    try:
        await db_session.delete(centro_treinamento)
        await db_session.commit()
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao deletar o centro de treinamento'
        )