from fastapi import APIRouter
from workout_api.atleta.controller import api_router as atleta_router

api_router = APIRouter()
api_router.include_router(atleta_router, prefix="/atleta", tags=["atleta"])
