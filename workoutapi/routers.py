from fastapi import APIRouter
from workout_api.atleta.controller import api_router as atleta_router
from workout_api.categorias.controller import api_router as categoria_router
from workout_api.centro_treinamento.controller import api_router as centro_treinamento_router

api_router = APIRouter()
api_router.include_router(atleta_router, prefix="/atleta", tags=["atleta"])
api_router.include_router(categoria_router, prefix="/categoria", tags=["categoria"])
api_router.include_router(centro_treinamento_router, prefix="/centro_treinamento", tags=["centro_treinamento"])    