import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from workout_api.atleta.controller import api_router as atleta_router
from workout_api.categorias.controller import api_router as categoria_router

# Configuração da aplicação
app = FastAPI(
    title="Workout API",
    description="API para gerenciamento de treinos e atletas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todos os routers
app.include_router(atleta_router, prefix="/atleta", tags=["atleta"])
app.include_router(categoria_router, prefix="/categoria", tags=["categoria"])

# Endpoint de health check
@app.get("/health")
async def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return {"status": "healthy", "message": "Workout API is running!"}

# Rotas principais da aplicação
@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Bem-vindo à Workout API",
        "docs": "/docs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    reload = os.getenv("API_RELOAD", "true").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        log_level="info",
        reload=reload
    )