# 🐳 Workout API - Instruções Docker Atualizadas

## 📋 Pré-requisitos

✅ **Docker Desktop instalado e rodando**  
✅ **Windows PowerShell** ou terminal equivalente  
✅ **Porta 5432 e 8000 disponíveis**

## 🚀 Como Executar

### **1. Inicialização Rápida**

```powershell
# Windows PowerShell (Recomendado)
.\commands.ps1 up

# Ou Docker tradicional
docker-compose up -d
```

### **2. Verificar Status**

```powershell
# Via script PowerShell
.\commands.ps1 status

# Via Docker direto
docker-compose ps
```

### **3. Ver Logs**

```powershell
# Logs da API
.\commands.ps1 logs

# Logs do banco de dados
.\commands.ps1 logs-db

# Todos os logs
docker-compose logs -f
```

## 🌐 Acessos após Inicialização

### **🎯 URLs Principais**

- **API Principal**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação Redoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### **🗃️ Banco PostgreSQL**

- **Host**: localhost
- **Porta**: 5432
- **Database**: workout
- **Usuário**: workout
- **Senha**: workout

### **🔧 PgAdmin (Opcional)**

```powershell
# Ativar interface web do PostgreSQL
.\commands.ps1 pgadmin-up

# Acessar: http://localhost:5050
# Email: admin@workoutapi.com
# Senha: admin123
```

## 📦 Comandos Essenciais

### **🚀 Gerenciamento da Aplicação**

```powershell
# === Comandos PowerShell (Windows) ===

# Iniciar aplicação
.\commands.ps1 up

# Parar aplicação
.\commands.ps1 down

# Status dos containers
.\commands.ps1 status

# Rebuild completo
.\commands.ps1 rebuild

# Ver logs em tempo real
.\commands.ps1 logs

# === Comandos Docker Diretos ===

# Iniciar aplicação
docker-compose up -d

# Parar aplicação
docker-compose down

# Status detalhado
docker-compose ps

# Rebuild de um serviço específico
docker-compose build workout_api

# Ver logs
docker-compose logs -f workout_api
```

### **🗃️ Comandos do Banco de Dados**

```powershell
# === Via Script PowerShell ===

# Conectar ao PostgreSQL
.\commands.ps1 db-shell

# Ver tabelas do banco
.\commands.ps1 db-tables

# Descrever estrutura da tabela atletas
.\commands.ps1 db-describe

# === Via Docker Direto ===

# Conectar ao banco
docker-compose exec workout_api_db psql -U workout -d workout

# Comandos SQL diretos
docker-compose exec workout_api_db psql -U workout -d workout -c "\dt"
docker-compose exec workout_api_db psql -U workout -d workout -c "\d atletas"
docker-compose exec workout_api_db psql -U workout -d workout -c "SELECT version();"
```

### **🔄 Migrações com Alembic**

```powershell
# === Via Script PowerShell ===

# Aplicar migrações
.\commands.ps1 migrate

# Criar nova migração
.\commands.ps1 create-migrations -d "descricao_da_mudanca"

# Ver status atual
.\commands.ps1 migration-status

# Ver histórico
.\commands.ps1 migration-history

# Rollback (voltar uma migração)
.\commands.ps1 rollback

# === Via Docker Direto ===

# Aplicar migrações
docker-compose exec workout_api alembic upgrade head

# Criar migração
docker-compose exec workout_api alembic revision --autogenerate -m "descricao"

# Status e histórico
docker-compose exec workout_api alembic current
docker-compose exec workout_api alembic history
```

## 🏗️ Estrutura dos Containers

### **📊 Serviços Configurados**

| Serviço            | Container            | Porta | Função                  |
| ------------------ | -------------------- | ----- | ----------------------- |
| **workout_api**    | workout_api_app      | 8000  | API FastAPI             |
| **workout_api_db** | workout_api_database | 5432  | PostgreSQL              |
| **pgadmin**        | workout_api_pgadmin  | 5050  | Interface DB (opcional) |

### **🔗 Configuração de Rede**

```yaml
Network: workout_network (bridge)
├── workout_api_app      (Internal: workout_api:8000)
├── workout_api_database (Internal: workout_api_db:5432)
└── workout_api_pgadmin  (Internal: pgadmin:80)
```

### **💾 Volumes Persistentes**

- `workout_postgres_data` → Dados do PostgreSQL
- `workout_pgadmin_data` → Configurações do PgAdmin

## 🛠️ Comandos de Desenvolvimento

### **🧪 Testes e Qualidade**

```powershell
# Executar testes
.\commands.ps1 test

# Formatar código com black
.\commands.ps1 format

# Lint com flake8
.\commands.ps1 lint

# Acessar shell da aplicação
.\commands.ps1 shell
```

### **🔧 Comandos de Manutenção**

```powershell
# Backup do banco
.\commands.ps1 backup-db

# Resetar banco (CUIDADO: apaga dados)
.\commands.ps1 db-reset

# Limpar recursos Docker
.\commands.ps1 clean

# Testar endpoints da API
.\commands.ps1 test-api
```

## 🔍 Resolução de Problemas

### **❌ Container não inicia**

```powershell
# Verificar logs detalhados
.\commands.ps1 logs

# Rebuildar imagens
.\commands.ps1 rebuild

# Verificar se portas estão livres
netstat -an | findstr "8000"
netstat -an | findstr "5432"
```

### **❌ Problemas com banco de dados**

```powershell
# Ver logs do PostgreSQL
.\commands.ps1 logs-db

# Resetar banco completamente
.\commands.ps1 db-reset

# Verificar conectividade
.\commands.ps1 db-shell
```

### **❌ Erro de permissões**

```powershell
# Parar tudo e reiniciar
docker-compose down -v
docker-compose up -d

# Limpar cache Docker
docker system prune -f
```

### **❌ Porta já em uso**

Se as portas 8000 ou 5432 estão ocupadas, edite `docker-compose.yml`:

```yaml
services:
  workout_api:
    ports:
      - "8001:8000" # Mudar para 8001

  workout_api_db:
    ports:
      - "5433:5432" # Mudar para 5433
```

## ✅ Validação Completa

### **1. Verificar Containers**

```powershell
.\commands.ps1 status
```

**Resultado esperado:**

```
NAME                   STATUS          PORTS
workout_api_app        Up (healthy)    0.0.0.0:8000->8000/tcp
workout_api_database   Up (healthy)    0.0.0.0:5432->5432/tcp
```

### **2. Testar API**

```powershell
# Via script
.\commands.ps1 test-api

# Via browser
# http://localhost:8000
# http://localhost:8000/docs
```

### **3. Verificar Banco**

```powershell
# Listar tabelas
.\commands.ps1 db-tables
```

**Resultado esperado:**

```
public | alembic_version    | table | workout
public | atletas            | table | workout
public | categorias         | table | workout
public | centro_treinamento | table | workout
```

## 🎯 Comandos de Uso Diário

### **🌅 Rotina Matinal (Iniciar Trabalho)**

```powershell
# Iniciar aplicação
.\commands.ps1 up

# Ver se está tudo OK
.\commands.ps1 status

# Acessar documentação
start http://localhost:8000/docs
```

### **🌙 Rotina Noturna (Finalizar Trabalho)**

```powershell
# Fazer backup (opcional)
.\commands.ps1 backup-db

# Parar aplicação
.\commands.ps1 down
```

### **🔄 Deploy de Mudanças**

```powershell
# 1. Modificar código
# 2. Criar migração se necessário
.\commands.ps1 create-migrations -d "mudanca_realizada"

# 3. Rebuildar e aplicar
.\commands.ps1 rebuild
.\commands.ps1 migrate

# 4. Testar
.\commands.ps1 test-api
```

## 📚 Comandos de Referência Rápida

```powershell
# === BÁSICOS ===
.\commands.ps1 up           # ⬆️ Iniciar
.\commands.ps1 down         # ⬇️ Parar
.\commands.ps1 status       # 📊 Status
.\commands.ps1 logs         # 📋 Ver logs

# === BANCO ===
.\commands.ps1 db-shell     # 🗃️ Conectar PostgreSQL
.\commands.ps1 db-tables    # 📋 Listar tabelas
.\commands.ps1 migrate      # 🔄 Aplicar migrações

# === DESENVOLVIMENTO ===
.\commands.ps1 shell        # 🐚 Shell da aplicação
.\commands.ps1 test         # 🧪 Executar testes
.\commands.ps1 rebuild      # 🔨 Rebuildar tudo

# === UTILITÁRIOS ===
.\commands.ps1 backup-db    # 💾 Backup
.\commands.ps1 pgadmin-up   # 🌐 Interface web DB
.\commands.ps1 help         # ❓ Ver todos os comandos
```

---

**🏆 Com esses comandos, você tem controle total sobre a Workout API via Docker!**
