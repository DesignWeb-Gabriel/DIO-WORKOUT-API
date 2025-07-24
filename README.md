# 🏋️ Workout API - Sistema Completo de Gerenciamento de Atletas

Uma **API REST profissional e completa** para gerenciamento de atletas, categorias e centros de treinamento, desenvolvida com **FastAPI**, **PostgreSQL**, **Docker** e **SQLAlchemy**.

## 🌟 **Status: PRODUÇÃO READY - CRUD COMPLETO IMPLEMENTADO**

✅ **Sistema 100% funcional** com todas as operações CRUD  
✅ **Relacionamentos bidirecionais** entre entidades  
✅ **Validações robustas** e tratamento de erros  
✅ **Dockerizado** com PostgreSQL  
✅ **Migrações automáticas** com Alembic

---

## 📋 Funcionalidades Implementadas

### 🏃 **Módulo Atletas - CRUD Completo**

- ✅ **Criar atleta** com validação de CPF único
- ✅ **Listar todos os atletas** com categorias e centros
- ✅ **Buscar atleta por ID** com relacionamentos
- ✅ **Atualizar atleta** (campos opcionais)
- ✅ **Deletar atleta** com validações

### 🏆 **Módulo Categorias - CRUD Completo**

- ✅ **Criar categoria** com validação de nome único
- ✅ **Listar todas as categorias**
- ✅ **Buscar categoria por ID**
- ✅ **Atualizar categoria** com validações
- ✅ **Deletar categoria**

### 🏢 **Módulo Centros de Treinamento - CRUD Completo**

- ✅ **Criar centro** com validação de nome único
- ✅ **Listar todos os centros**
- ✅ **Buscar centro por ID**
- ✅ **Atualizar centro** com validações
- ✅ **Deletar centro**

### 🔗 **Relacionamentos e Validações**

- ✅ **Foreign Keys** funcionais entre todas as entidades
- ✅ **Validação de CPF único** para atletas
- ✅ **Validação de nomes únicos** para categorias e centros
- ✅ **Campos obrigatórios** validados via Pydantic
- ✅ **Tratamento de erros** com códigos HTTP apropriados
- ✅ **Rollback automático** em caso de falha

---

## 🚀 Tecnologias e Arquitetura

| Categoria           | Tecnologia     | Versão    | Função                       | Status      |
| ------------------- | -------------- | --------- | ---------------------------- | ----------- |
| **Backend**         | FastAPI        | 0.116.1   | Framework web moderno        | ✅ Produção |
| **Banco**           | PostgreSQL     | 16-alpine | Banco relacional             | ✅ Produção |
| **ORM**             | SQLAlchemy     | 2.0.41    | Mapeamento objeto-relacional | ✅ Produção |
| **Migrações**       | Alembic        | 1.14.0    | Controle de versão do DB     | ✅ Produção |
| **Containerização** | Docker Compose | Latest    | Orquestração de serviços     | ✅ Produção |
| **Validação**       | Pydantic       | 2.11.7    | Validação e serialização     | ✅ Produção |
| **Servidor**        | Uvicorn        | 0.35.0    | Servidor ASGI                | ✅ Produção |

## 🏗️ Arquitetura do Sistema

```
🌐 FastAPI API (Port 8000) - CRUD COMPLETO
    ├── 🏃 /atleta/** - 5 endpoints (POST, GET, GET/{id}, PATCH, DELETE)
    │   ├── Validação CPF único ✅
    │   ├── Relacionamentos com categoria e centro ✅
    │   └── Update parcial (nome, idade, peso, altura) ✅
    │
    ├── 🏆 /categoria/** - 5 endpoints (POST, GET, GET/{id}, PATCH, DELETE)
    │   ├── Validação nome único ✅
    │   └── Relacionamento com atletas ✅
    │
    └── 🏢 /centro_treinamento/** - 5 endpoints (POST, GET, GET/{id}, PATCH, DELETE)
        ├── Validação nome único ✅
        ├── Campos: nome, endereço, proprietário ✅
        └── Relacionamento com atletas ✅
                    ↓
🗃️ PostgreSQL (Port 5432) - RELACIONAL COMPLETO
    ├── Tabela: atletas (com FK para categorias e centros) ✅
    ├── Tabela: categorias (relacionamento 1:N com atletas) ✅
    ├── Tabela: centro_treinamento (relacionamento 1:N com atletas) ✅
    ├── Campos: created_at, updated_at em todas as tabelas ✅
    └── Tabela: alembic_version (controle de migrações) ✅
```

## 🔧 Pré-requisitos

- **Docker Desktop** instalado e rodando
- **Git**
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
- **Documentação**: http://localhost:8000/docs ⭐ **Swagger com todos os endpoints**
- **Redoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

---

## 🌐 API Endpoints - CRUD Completo

### **🏃 Atletas (/atleta)**

| Método | Endpoint       | Função                   | Validações                        |
| ------ | -------------- | ------------------------ | --------------------------------- |
| POST   | `/atleta/`     | Criar novo atleta        | CPF único, categoria/centro exist |
| GET    | `/atleta/`     | Listar todos os atletas  | Com relações carregadas           |
| GET    | `/atleta/{id}` | Buscar atleta específico | UUID válido                       |
| PATCH  | `/atleta/{id}` | Atualizar atleta         | Campos opcionais                  |
| DELETE | `/atleta/{id}` | Deletar atleta           | Cascade seguro                    |

### **🏆 Categorias (/categoria)**

| Método | Endpoint          | Função                      | Validações    |
| ------ | ----------------- | --------------------------- | ------------- |
| POST   | `/categoria/`     | Criar nova categoria        | Nome único    |
| GET    | `/categoria/`     | Listar todas as categorias  | -             |
| GET    | `/categoria/{id}` | Buscar categoria específica | UUID válido   |
| PATCH  | `/categoria/{id}` | Atualizar categoria         | Nome único    |
| DELETE | `/categoria/{id}` | Deletar categoria           | Verificar uso |

### **🏢 Centros de Treinamento (/centro_treinamento)**

| Método | Endpoint                   | Função                   | Validações    |
| ------ | -------------------------- | ------------------------ | ------------- |
| POST   | `/centro_treinamento/`     | Criar novo centro        | Nome único    |
| GET    | `/centro_treinamento/`     | Listar todos os centros  | -             |
| GET    | `/centro_treinamento/{id}` | Buscar centro específico | UUID válido   |
| PATCH  | `/centro_treinamento/{id}` | Atualizar centro         | Nome único    |
| DELETE | `/centro_treinamento/{id}` | Deletar centro           | Verificar uso |

---

## 📊 Modelos de Dados

### **🏃 Atleta**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "nome": "João da Silva",
  "cpf": "12345678901",
  "idade": 25,
  "peso": 75.5,
  "altura": 1.8,
  "sexo": "M",
  "created_at": "2025-01-19T10:30:00Z",
  "updated_at": "2025-01-19T10:30:00Z",
  "categoria": {
    "id": "550e8400-e29b-41d4-a716-446655440001",
    "nome": "Intermediário",
    "created_at": "2025-01-19T10:30:00Z",
    "updated_at": "2025-01-19T10:30:00Z"
  },
  "centro_treinamento": {
    "id": "550e8400-e29b-41d4-a716-446655440002",
    "nome": "Academia Central",
    "endereco": "Rua das Flores, 123",
    "proprietario": "Maria Santos",
    "created_at": "2025-01-19T10:30:00Z",
    "updated_at": "2025-01-19T10:30:00Z"
  }
}
```

### **🏆 Categoria**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440001",
  "nome": "Intermediário",
  "created_at": "2025-01-19T10:30:00Z",
  "updated_at": "2025-01-19T10:30:00Z"
}
```

### **🏢 Centro de Treinamento**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440002",
  "nome": "Academia Central",
  "endereco": "Rua das Flores, 123, São Paulo, SP",
  "proprietario": "Maria Santos",
  "created_at": "2025-01-19T10:30:00Z",
  "updated_at": "2025-01-19T10:30:00Z"
}
```

---

## 💡 Exemplos de Uso da API

### **🏃 Criar Atleta**

```bash
curl -X POST "http://localhost:8000/atleta/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João da Silva",
    "cpf": "12345678901",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.80,
    "sexo": "M",
    "categoria": "Intermediário",
    "centro_treinamento": "Academia Central"
  }'
```

### **🏆 Criar Categoria**

```bash
curl -X POST "http://localhost:8000/categoria/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Avançado"
  }'
```

### **🏢 Criar Centro de Treinamento**

```bash
curl -X POST "http://localhost:8000/centro_treinamento/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Academia Fitness Pro",
    "endereco": "Av. Paulista, 1000, São Paulo, SP",
    "proprietario": "Carlos Alberto"
  }'
```

### **📝 Atualizar Atleta (Parcial)**

```bash
curl -X PATCH "http://localhost:8000/atleta/{id}" \
  -H "Content-Type: application/json" \
  -d '{
    "peso": 78.0,
    "altura": 1.82
  }'
```

---

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

### **Tabelas Criadas (Todas Funcionais)**

- ✅ `atletas` - Dados dos atletas com FKs
- ✅ `categorias` - Categorias esportivas
- ✅ `centro_treinamento` - Locais de treino
- ✅ `alembic_version` - Controle de migrações

### **Relacionamentos Implementados**

```sql
-- Tabela atletas com Foreign Keys
CREATE TABLE atletas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    idade INTEGER NOT NULL,
    peso FLOAT NOT NULL,
    altura FLOAT NOT NULL,
    sexo VARCHAR(1) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    categoria_id UUID REFERENCES categorias(id),
    centro_treinamento_id UUID REFERENCES centro_treinamento(id)
);

-- Índices para performance
CREATE INDEX idx_atletas_cpf ON atletas(cpf);
CREATE INDEX idx_atletas_categoria ON atletas(categoria_id);
CREATE INDEX idx_atletas_centro ON atletas(centro_treinamento_id);
```

---

## 🔄 Comandos Úteis

### **PowerShell Script (Windows - Recomendado)**

```powershell
# === APLICAÇÃO ===
.\commands.ps1 help                    # Ver todos os comandos
.\commands.ps1 up                      # Iniciar aplicação
.\commands.ps1 down                    # Parar aplicação
.\commands.ps1 status                  # Status dos containers
.\commands.ps1 logs                    # Ver logs da API
.\commands.ps1 restart                 # Reiniciar aplicação

# === BANCO DE DADOS ===
.\commands.ps1 db-tables               # Listar tabelas
.\commands.ps1 db-shell                # Acessar PostgreSQL
.\commands.ps1 db-describe             # Estrutura das tabelas
.\commands.ps1 pgadmin-up              # Abrir PgAdmin (http://localhost:5050)
.\commands.ps1 backup-db               # Backup do banco

# === MIGRAÇÕES ===
.\commands.ps1 create-migrations -d "descricao"  # Criar migração
.\commands.ps1 migrate                           # Aplicar migrações
.\commands.ps1 migration-status                  # Status atual
.\commands.ps1 rollback                          # Reverter última

# === DESENVOLVIMENTO ===
.\commands.ps1 shell                   # Acessar container da API
.\commands.ps1 test                    # Executar testes
.\commands.ps1 format                  # Formatar código
.\commands.ps1 rebuild                 # Rebuild completo
```

### **Docker Direto (Multiplataforma)**

```bash
# APLICAÇÃO
docker-compose up -d                   # Iniciar
docker-compose down                    # Parar
docker-compose ps                      # Status
docker-compose logs -f workout_api     # Logs

# MIGRAÇÕES
docker-compose exec workout_api alembic revision --autogenerate -m "descricao"
docker-compose exec workout_api alembic upgrade head
docker-compose exec workout_api alembic current

# BANCO DE DADOS
docker-compose exec workout_api_db psql -U workout -d workout -c "\dt"
docker-compose exec workout_api_db psql -U workout -d workout -c "\d atletas"
```

### **Makefile (Linux/Mac/WSL)**

```bash
make help                              # Ver comandos
make up                                # Iniciar aplicação
make migrate                           # Aplicar migrações
make db-tables                         # Ver tabelas
make logs                              # Ver logs
make test                              # Executar testes
```

---

## 📊 Estrutura do Projeto Completa

```
DIO WORKOUT API/
├── 🐳 docker-compose.yml              # Orquestração de containers
├── 📝 README.md                       # Este arquivo (atualizado)
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
    ├── 🔗 routers.py                 # Configuração de rotas
    └── 🏃 workout_api/               # Código principal
        ├── main.py                   # Aplicação FastAPI
        ├── contrib/                  # Modelos e schemas base
        │   ├── models.py            # BaseModel com UUID
        │   ├── schemas.py           # BaseSchema, OutMixin
        │   └── dependencies.py      # Database dependency
        ├── atleta/                   # Módulo atleta COMPLETO
        │   ├── models.py            # AtletaModel com FKs ✅
        │   ├── schemas.py           # AtletaIn, AtletaOut, AtletaUpdate ✅
        │   └── controller.py        # CRUD completo ✅
        ├── categorias/               # Módulo categorias COMPLETO
        │   ├── models.py            # CategoriaModel ✅
        │   ├── schemas.py           # CategoriaIn, CategoriaOut ✅
        │   └── controller.py        # CRUD completo ✅
        └── centro_treinamento/       # Módulo centros COMPLETO
            ├── models.py            # CentroTreinamentoModel ✅
            ├── schemas.py           # CentroTreinamentoIn/Out ✅
            └── controller.py        # CRUD completo ✅
```

---

## 🛡️ Validações e Segurança Implementadas

### **🔒 Validações de Integridade**

- ✅ **CPF único** - Não permite atletas duplicados
- ✅ **Nomes únicos** - Categorias e centros não podem ter nomes iguais
- ✅ **Foreign Keys** - Integridade referencial entre tabelas
- ✅ **Campos obrigatórios** - Validação via Pydantic
- ✅ **Tipos de dados** - Validação de UUID, Float, String, etc.

### **🛡️ Tratamento de Erros**

- ✅ **400 Bad Request** - Dados inválidos ou faltando
- ✅ **404 Not Found** - Recurso não encontrado
- ✅ **409 Conflict** - Violação de unicidade (CPF, nomes)
- ✅ **500 Internal Server Error** - Erros de servidor
- ✅ **Rollback automático** - Transações revertidas em caso de erro

### **⚡ Performance e Segurança**

- ✅ **Connection pooling** - SQLAlchemy gerencia conexões
- ✅ **Prepared statements** - Proteção contra SQL injection
- ✅ **UUID como PK** - IDs não sequenciais para segurança
- ✅ **Lazy loading** - Relacionamentos carregados sob demanda

---

## 🧪 Testando a API

### **1. Via Swagger UI (Recomendado)**

Acesse http://localhost:8000/docs e teste todos os endpoints interativamente:

1. **Criar categoria**: `POST /categoria/` com `{"nome": "Intermediário"}`
2. **Criar centro**: `POST /centro_treinamento/` com dados completos
3. **Criar atleta**: `POST /atleta/` referenciando categoria e centro pelos nomes
4. **Listar atletas**: `GET /atleta/` - deve mostrar atleta com relações carregadas
5. **Atualizar atleta**: `PATCH /atleta/{id}` com dados parciais

### **2. Via cURL**

```bash
# 1. Criar categoria
curl -X POST "http://localhost:8000/categoria/" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Intermediário"}'

# 2. Criar centro
curl -X POST "http://localhost:8000/centro_treinamento/" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Academia Central", "endereco": "Rua A, 123", "proprietario": "João"}'

# 3. Criar atleta
curl -X POST "http://localhost:8000/atleta/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Maria Silva",
    "cpf": "12345678901",
    "idade": 25,
    "peso": 65.0,
    "altura": 1.70,
    "sexo": "F",
    "categoria": "Intermediário",
    "centro_treinamento": "Academia Central"
  }'

# 4. Listar atletas (deve mostrar com relações)
curl "http://localhost:8000/atleta/"
```

### **3. Validar Funcionamento**

```powershell
# Verificar tabelas no banco
.\commands.ps1 db-tables

# Ver logs da aplicação
.\commands.ps1 logs

# Testar health check
curl http://localhost:8000/health
```

---

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

# Acessar shell do container
.\commands.ps1 shell
```

### **Adicionando Novas Funcionalidades**

```powershell
# 1. Modificar modelos em workout_api/*/models.py
# 2. Criar migração
.\commands.ps1 create-migrations -d "adicionar_nova_coluna"
# 3. Aplicar migração
.\commands.ps1 migrate
# 4. Atualizar schemas em */schemas.py
# 5. Atualizar controllers em */controller.py
# 6. Testar via Swagger
```

---

## 🔍 Resolução de Problemas

### **🐳 Docker não inicia**

```powershell
# Verificar se Docker Desktop está rodando
docker --version
# Rebuildar se necessário
.\commands.ps1 rebuild
# Verificar portas livres
netstat -an | findstr "8000\|5432"
```

### **🗃️ Erro de conexão no banco**

```powershell
# Resetar banco de dados
.\commands.ps1 down
.\commands.ps1 up
# Verificar containers
.\commands.ps1 status
# Testar conexão
.\commands.ps1 db-shell
```

### **🔄 Problemas com migrações**

```powershell
# Ver status atual
.\commands.ps1 migration-status
# Forçar migração
docker-compose exec workout_api alembic stamp head
.\commands.ps1 migrate
```

### **⚡ Performance Issues**

```powershell
# Limpar cache Docker
docker system prune -f
# Rebuild completo
.\commands.ps1 rebuild
```

---

## 📈 Funcionalidades Implementadas vs Planejadas

### ✅ **IMPLEMENTADO (Produção Ready)**

- [x] **CRUD completo para Atletas** (5 endpoints)
- [x] **CRUD completo para Categorias** (5 endpoints)
- [x] **CRUD completo para Centros de Treinamento** (5 endpoints)
- [x] **Relacionamentos bidirecionais** entre entidades
- [x] **Validações robustas** (CPF único, nomes únicos)
- [x] **Tratamento de erros** com códigos HTTP apropriados
- [x] **Campos timestamp** (created_at, updated_at)
- [x] **Migrações automáticas** com Alembic
- [x] **Documentação Swagger** interativa
- [x] **Dockerização completa** com PostgreSQL
- [x] **Rollback de transações** em caso de erro

### 🚧 **Próximas Funcionalidades Planejadas**

- [ ] Sistema de autenticação JWT
- [ ] Filtros avançados e paginação nos endpoints GET
- [ ] API de estatísticas e relatórios
- [ ] Upload de imagens de atletas
- [ ] Sistema de notificações
- [ ] Cache com Redis
- [ ] Testes automatizados completos
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em produção (AWS/GCP)

---

## ⚠️ Observações Pessoais e Aprendizados

Durante o desenvolvimento, enfrentei alguns desafios devido à abordagem adotada no curso:

- Muitos passos técnicos foram subentendidos, como o uso de `pyenv`, `Makefile`, Alembic e DBeaver, o que exigiu pesquisa externa para entender.
- A maior parte dos comandos foi apresentada com base em sistemas Linux, o que dificultou o processo para usuários Windows/macOS (como eu).
- Alguns erros e bugs aparecem ao longo do desenvolvimento e só são corrigidos em vídeos futuros, causando confusão para quem segue a linha cronológica das aulas.
- Apesar disso, consegui concluir o projeto com sucesso graças ao meu conhecimento prévio de Docker e PostgreSQL, e ao suporte de IA para entender e corrigir falhas.

Essas dificuldades me ajudaram a desenvolver ainda mais autonomia técnica, reforçando minha capacidade de aprender de forma independente e solucionar problemas em ambientes complexos.

---

## 📚 Documentação Adicional

- [`CONFIGURACAO_COMPLETA.md`](CONFIGURACAO_COMPLETA.md) - Configuração técnica detalhada
- [`DOCKER_INSTRUCTIONS.md`](DOCKER_INSTRUCTIONS.md) - Instruções Docker
- [`DBEAVER_CONNECTION.md`](DBEAVER_CONNECTION.md) - Configuração DBeaver
- [`ALEMBIC_COMMANDS.md`](ALEMBIC_COMMANDS.md) - Comandos Alembic
- [`WINDOWS_SETUP.md`](WINDOWS_SETUP.md) - Setup para Windows
- [`ATUALIZACOES_ARQUIVOS_MD.md`](ATUALIZACOES_ARQUIVOS_MD.md) - Log de mudanças

---

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Add nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Desenvolvido durante o Bootcamp DIO (Digital Innovation One)**

- 🚀 **Status**: ✅ **PRODUÇÃO READY - CRUD COMPLETO IMPLEMENTADO**
- 📅 **Última Atualização**: Janeiro 2025
- ⚡ **Versão**: 2.0.0 - CRUD COMPLETO
- 🏆 **Funcionalidades**: 15 endpoints funcionais + relacionamentos

---

## 🎯 Quick Start

```powershell
# 1. Iniciar aplicação
.\commands.ps1 up

# 2. Acessar documentação
# http://localhost:8000/docs

# 3. Testar API (criar categoria, centro, atleta)
# Via Swagger UI - interface visual completa

# 4. Verificar banco
.\commands.ps1 db-tables
```

---

**🏆 Sistema profissional COMPLETO de gerenciamento de atletas com CRUD funcional, relacionamentos e validações robustas!**

**⚡ PRONTO PARA PRODUÇÃO** - Todos os endpoints testados e funcionais!
