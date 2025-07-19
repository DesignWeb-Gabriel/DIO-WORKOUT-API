# ==============================================================================
# Workout API - Dockerfile
# ==============================================================================

# Imagem base otimizada para Python
FROM python:3.11-slim

# Metadados
LABEL maintainer="Workout API Team"
LABEL version="1.0"
LABEL description="API para gerenciamento de treinos e atletas"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Criar usuário não-root para segurança
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY workout_api/ ./workout_api/

# Copiar arquivos do Alembic
COPY alembic.ini .
COPY alembic/ ./alembic/

# Alterar proprietário dos arquivos
RUN chown -R appuser:appgroup /app

# Mudar para usuário não-root
USER appuser

# Expor porta da aplicação
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/docs || exit 1

# Comando para executar a aplicação
CMD ["uvicorn", "workout_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 