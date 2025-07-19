# 🐳 Workout API - Instruções Docker

## 📋 Pré-requisitos

- Docker instalado
- Docker Compose instalado

## 🚀 Como executar

### 1. Executar a aplicação completa

```bash
# Na pasta raiz do projeto (DIO WORKOUT API)
docker-compose up -d
```

### 2. Verificar se os containers estão funcionando

```bash
docker-compose ps
```

### 3. Ver logs da aplicação

```bash
# Logs da API
docker-compose logs workout_api

# Logs do banco de dados
docker-compose logs workout_api_db

# Todos os logs
docker-compose logs -f
```

## 🌐 Acessos

- **API**: http://localhost:8000
- **Documentação (Swagger)**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **Banco PostgreSQL**: localhost:5432

### 🔧 PgAdmin (Opcional)

Para usar o PgAdmin (interface web para PostgreSQL):

```bash
# Executar com PgAdmin
docker-compose --profile tools up -d
```

- **PgAdmin**: http://localhost:5050
  - Email: `admin@workoutapi.com`
  - Senha: `admin123`

## 🗃️ Configurações do Banco

- **Database**: `workout_api`
- **Usuário**: `workout_api`
- **Senha**: `workout_api_password`
- **Host**: `localhost` (ou `workout_api_db` dentro do container)
- **Porta**: `5432`

## 📦 Comandos úteis

```bash
# Parar os containers
docker-compose down

# Parar e remover volumes (CUIDADO: apaga dados do banco)
docker-compose down -v

# Rebuild da aplicação
docker-compose build workout_api

# Executar comandos dentro do container da API
docker-compose exec workout_api bash

# Ver logs em tempo real
docker-compose logs -f workout_api
```

## 🔍 Troubleshooting

### Container não inicia

```bash
# Ver logs detalhados
docker-compose logs workout_api

# Rebuildar a imagem
docker-compose build --no-cache workout_api
```

### Problemas com banco de dados

```bash
# Resetar o volume do banco
docker-compose down -v
docker-compose up -d
```

### Porta já em uso

Se a porta 8000 ou 5432 já estiver em uso, edite o `docker-compose.yml` e altere as portas:

```yaml
ports:
  - "8001:8000" # Para a API
  # ou
  - "5433:5432" # Para o PostgreSQL
```

## ✅ Validação

Para verificar se tudo está funcionando:

1. Acesse: http://localhost:8000
2. Deve retornar: `{"message": "Bem-vindo à Workout API", ...}`
3. Acesse: http://localhost:8000/docs
4. Deve abrir a documentação Swagger da API

## 🏗️ Estrutura dos Containers

- **workout_api_app**: Aplicação FastAPI
- **workout_api_database**: Banco PostgreSQL
- **workout_api_pgadmin**: Interface web para PostgreSQL (opcional)
