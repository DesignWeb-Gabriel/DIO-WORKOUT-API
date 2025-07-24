import uuid
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy import select
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from datetime import datetime
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DatabaseDependency

api_router = APIRouter()

@api_router.post(
    "/", 
    summary="Criar categoria", 
    status_code=status.HTTP_201_CREATED, 
    response_model=CategoriaOut
)
async def create_categoria(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    # Verificar se categoria já existe
    categoria_exists = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_in.nome)
    )).scalars().first()
    
    if categoria_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Já existe uma categoria com o nome: {categoria_in.nome}'
        )
    
    try:
        categoria_id = uuid.uuid4()
        categoria_model = CategoriaModel(
            id=categoria_id,
            nome=categoria_in.nome,
            created_at=datetime.utcnow()
        )

        db_session.add(categoria_model)
        await db_session.commit()
        await db_session.refresh(categoria_model)
        
        return CategoriaOut(
            id=categoria_model.id,
            nome=categoria_model.nome,
            created_at=categoria_model.created_at,
            updated_at=categoria_model.updated_at
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao criar a categoria'
        )

@api_router.get("/", summary="Listar categorias",
                status_code=status.HTTP_200_OK,
                response_model=list[CategoriaOut])
async def get_categorias(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return [CategoriaOut(
        id=categoria.id,
        nome=categoria.nome,
        created_at=categoria.created_at,
        updated_at=categoria.updated_at
    ) for categoria in categorias]

@api_router.get("/{categoria_id}", summary="Buscar categoria por ID",
                status_code=status.HTTP_200_OK,
                response_model=CategoriaOut)
async def get_categoria_by_id(categoria_id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria = (await db_session.execute(
        select(CategoriaModel).where(CategoriaModel.id == categoria_id)
    )).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Categoria não encontrada"
        )
    
    return CategoriaOut(
        id=categoria.id,
        nome=categoria.nome,
        created_at=categoria.created_at,
        updated_at=categoria.updated_at
    )

@api_router.patch("/{categoria_id}", summary="Atualizar categoria",
                 status_code=status.HTTP_200_OK,
                 response_model=CategoriaOut)
async def update_categoria(categoria_id: UUID4, db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria = (await db_session.execute(
        select(CategoriaModel).where(CategoriaModel.id == categoria_id)
    )).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    
    # Verificar se novo nome já existe em outra categoria
    if categoria_in.nome != categoria.nome:
        nome_exists = (await db_session.execute(
            select(CategoriaModel).filter_by(nome=categoria_in.nome)
        )).scalars().first()
        
        if nome_exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Já existe uma categoria com o nome: {categoria_in.nome}'
            )
    
    try:
        categoria.nome = categoria_in.nome
        await db_session.commit()
        await db_session.refresh(categoria)
        
        return CategoriaOut(
            id=categoria.id,
            nome=categoria.nome,
            created_at=categoria.created_at,
            updated_at=categoria.updated_at
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao atualizar a categoria'
        )

@api_router.delete("/{categoria_id}", summary="Deletar categoria",
                  status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria(categoria_id: UUID4, db_session: DatabaseDependency) -> None:
    categoria = (await db_session.execute(
        select(CategoriaModel).where(CategoriaModel.id == categoria_id)
    )).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    
    try:
        await db_session.delete(categoria)
        await db_session.commit()
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao deletar a categoria'
        )