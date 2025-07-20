# 🏋️ Workout API - Sistema de Gerenciamento de Atletas

Uma API REST profissional para gerenciamento de atletas, categorias e centros de treinamento, desenvolvida com **FastAPI**, **PostgreSQL** e **Docker**.

## 📋 Visão Geral

Sistema completo de gerenciamento esportivo com:

- **Cadastro de Atletas** com informações detalhadas (CPF, idade, peso, altura)
- **Categorias de Atletas** (iniciante, intermediário, avançado)
- **Centros de Treinamento** com endereço e proprietário
- **Relacionamentos entre entidades** com foreign keys
- **Migrações automáticas** com Alembic
- **Containerização completa** com Docker Compose

## 🚀 Tecnologias e Arquitetura

| Categoria           | Tecnologia     | Versão    | Função                       |
| ------------------- | -------------- | --------- | ---------------------------- |
| **Backend**         | FastAPI        | 0.116.1   | Framework web moderno        |
| **Banco**           | PostgreSQL     | 16-alpine | Banco relacional             |
| **ORM**             | SQLAlchemy     | 2.0.41    | Mapeamento objeto-relacional |
| **Migrações**       | Alembic        | 1.14.0    | Controle de versão do DB     |
| **Containerização** | Docker Compose | Latest    | Orquestração de serviços     |
| **Validação**       | Pydantic       | 2.11.7    | Validação e serialização     |
| **Servidor**        | Uvicorn        | 0.35.0    | Servidor ASGI                |

## 🏗️ Arquitetura do Sistema

```
🌐 FastAPI (Port 8000)
    ├── 🏃 Atletas (CPF, idade, peso, altura)
    ├── 🏆 Categorias (iniciante, intermediário, avançado)
    └── 🏢 Centros de Treinamento (endereço, proprietário)
                    ↓
🗃️ PostgreSQL (Port 5432)
    ├── Tabela: atletas
    ├── Tabela: categorias
    ├── Tabela: centro_treinamento
    └── Tabela: alembic_version (controle de migrações)
```

## 🔧 Pré-requisitos

- **Docker Desktop** instalado e rodando
- **Git** (opcional)
- **Windows 10+** / **macOS** / **Linux**

## 🚀 Instalação e Execução

### **1. Obter o Projeto**

```bash
git clone <repositorio>
cd "DIO WORKOUT API"
```

### **2. Inicializar Aplicação**

```powershell
# Windows PowerShell (Recomendado)
.\commands.ps1 up

# Ou Docker direto
docker-compose up -d
```

### **3. Verificar Status**

```powershell
# Via script
.\commands.ps1 status

# Via Docker
docker-compose ps
```

### **4. Acessar Aplicação**

- **API**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🗃️ Banco de Dados

### **Credenciais PostgreSQL**

```
Host: localhost
Port: 5432
Database: workout
Username: workout
Password: workout
SSL: Desabilitado
```

### **Tabelas Criadas**

- ✅ `atletas` - Dados dos atletas
- ✅ `categorias` - Categorias esportivas
- ✅ `centro_treinamento` - Locais de treino
- ✅ `alembic_version` - Controle de migrações

### **Conectar via DBeaver**

1. Nova conexão PostgreSQL
2. Usar credenciais acima
3. **Importante**: Desmarcar "Use SSL"

## 🔄 Comandos Úteis

### **PowerShell Script (Windows)**

```powershell
# Gerais
.\commands.ps1 help                    # Ver todos os comandos
.\commands.ps1 up                      # Iniciar aplicação
.\commands.ps1 down                    # Parar aplicação
.\commands.ps1 status                  # Status dos containers
.\commands.ps1 logs                    # Ver logs da API

# Banco de Dados
.\commands.ps1 db-tables               # Listar tabelas
.\commands.ps1 db-shell                # Acessar PostgreSQL
.\commands.ps1 pgadmin-up              # Abrir PgAdmin (http://localhost:5050)

# Migrações
.\commands.ps1 create-migrations -d "descricao"  # Criar migração
.\commands.ps1 migrate                           # Aplicar migrações
.\commands.ps1 migration-status                  # Status atual

# Desenvolvimento
.\commands.ps1 shell                   # Acessar container da API
.\commands.ps1 test                    # Executar testes
.\commands.ps1 backup-db               # Backup do banco
```

### **Docker Direto (Multiplataforma)**

```bash
# Aplicação
docker-compose up -d                   # Iniciar
docker-compose down                    # Parar
docker-compose ps                      # Status
docker-compose logs -f workout_api     # Logs

# Migrações
docker-compose exec workout_api alembic revision --autogenerate -m "descricao"
docker-compose exec workout_api alembic upgrade head
docker-compose exec workout_api alembic current

# Banco de dados
docker-compose exec workout_api_db psql -U workout -d workout -c "\dt"
```

### **Makefile (Linux/Mac/WSL)**

```bash
make help                              # Ver comandos
make up                                # Iniciar aplicação
make migrate                           # Aplicar migrações
make db-tables                         # Ver tabelas
make logs                              # Ver logs
```

## 📊 Estrutura do Projeto

```
DIO WORKOUT API/
├── 🐳 docker-compose.yml              # Orquestração de containers
├── 📝 README.md                       # Este arquivo
├── ⚡ commands.ps1                    # Comandos PowerShell
├── 🔨 Makefile                        # Comandos make
├── 📚 *.md                           # Documentação completa
└── workoutapi/                        # Aplicação Python
    ├── 🐳 Dockerfile                  # Imagem da aplicação
    ├── 📦 requirements.txt            # Dependências
    ├── ⚙️ alembic.ini                # Configuração Alembic
    ├── 🔄 alembic/                   # Migrações do banco
    │   ├── env.py                    # Ambiente Alembic
    │   └── versions/                 # Arquivos de migração
    └── 🏃 workout_api/               # Código principal
        ├── main.py                   # Aplicação FastAPI
        ├── contrib/                  # Modelos base
        ├── atleta/                   # Módulo atleta
        ├── categorias/               # Módulo categorias
        └── centro_treinamento/       # Módulo centros
```

## 🌐 Endpoints da API

### **Endpoints Base**

- `GET /` - Página inicial
- `GET /health` - Health check
- `GET /docs` - Documentação Swagger
- `GET /redoc` - Documentação Redoc

### **Modelos de Dados**

#### **Atleta**

```python
{
    "pk_id": 1,
    "nome": "João Silva",
    "cpf": "12345678901",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.80,
    "sexo": "M",
    "created_at": "2025-07-19T10:30:00",
    "categoria_id": 1,
    "centro_treinamento_id": 1
}
```

#### **Categoria**

```python
{
    "pk_id": 1,
    "nome": "Intermediário"
}
```

#### **Centro de Treinamento**

```python
{
    "pk_id": 1,
    "nome": "Academia Central",
    "endereco": "Rua das Flores, 123",
    "proprietario": "Maria Santos"
}
```

## 🛠️ Desenvolvimento

### **Ambiente de Desenvolvimento**

```powershell
# Iniciar em modo desenvolvimento
.\commands.ps1 up
.\commands.ps1 logs

# Formatar código
.\commands.ps1 format

# Verificar qualidade
.\commands.ps1 lint

# Executar testes
.\commands.ps1 test
```

### **Criando Novas Migrações**

```powershell
# 1. Alterar modelos em workout_api/*/models.py
# 2. Criar migração
.\commands.ps1 create-migrations -d "adicionar_nova_coluna"
# 3. Aplicar migração
.\commands.ps1 migrate
# 4. Verificar resultado
.\commands.ps1 db-tables
```

## 🔍 Resolução de Problemas

### **Docker não inicia**

```powershell
# Verificar se Docker Desktop está rodando
docker --version
# Rebuildar se necessário
.\commands.ps1 rebuild
```

### **Erro de conexão no banco**

```powershell
# Resetar banco de dados
.\commands.ps1 db-reset
# Verificar containers
.\commands.ps1 status
```

### **Problemas com PowerShell**

```powershell
# Liberar política de execução
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Usar Docker direto
docker-compose up -d
```

## 📈 Próximas Funcionalidades

- [ ] Endpoints CRUD completos para Atletas
- [ ] Sistema de autenticação JWT
- [ ] Filtros avançados e paginação
- [ ] API de estatísticas e relatórios
- [ ] Upload de imagens de atletas
- [ ] Sistema de notificações
- [ ] Cache com Redis
- [ ] Testes automatizados completos
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em produção

## 📚 Documentação Adicional

- [`CONFIGURACAO_COMPLETA.md`](CONFIGURACAO_COMPLETA.md) - Configuração técnica detalhada
- [`DOCKER_INSTRUCTIONS.md`](DOCKER_INSTRUCTIONS.md) - Instruções Docker
- [`DBEAVER_CONNECTION.md`](DBEAVER_CONNECTION.md) - Configuração DBeaver
- [`ALEMBIC_COMMANDS.md`](ALEMBIC_COMMANDS.md) - Comandos Alembic
- [`WINDOWS_SETUP.md`](WINDOWS_SETUP.md) - Setup para Windows

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Desenvolvido durante o Bootcamp DIO (Digital Innovation One)**

- 🚀 **Status**: Produção Ready
- 📅 **Última Atualização**: Julho 2025
- ⚡ **Versão**: 1.0.0

---

**🏆 Sistema profissional de gerenciamento de atletas com arquitetura moderna e escalável!**
