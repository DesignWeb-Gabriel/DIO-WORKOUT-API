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
async def create_categoria(db: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(
        id=uuid.uuid4(),
        **categoria_in.model_dump(),
    )
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db.add(categoria_model)
    await db.commit()
    return categoria_out

@api_router.get("/", summary="Listar categorias",
                status_code=status.HTTP_200_OK,
                response_model=list[CategoriaOut])
async def get_categoria(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias = list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return categorias

@api_router.get("/{categoria_id}", summary="Buscar categoria por ID",
                status_code=status.HTTP_200_OK,
                response_model=CategoriaOut)
async def get_categoria_by_id(categoria_id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria = CategoriaOut  = (await db_session.execute(select(CategoriaModel).where(CategoriaModel.id == categoria_id))).scalars().first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada")
    return categoria