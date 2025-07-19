# 🗃️ Alembic - Comandos para Windows

## 🐳 **Opção 1: Via Docker (Recomendado)**

### **Inicializar Alembic**

```powershell
docker-compose exec workout_api alembic init alembic
```

### **Criar primeira migração**

```powershell
docker-compose exec workout_api alembic revision --autogenerate -m "initial_migration"
```

### **Aplicar migrações**

```powershell
docker-compose exec workout_api alembic upgrade head
```

### **Ver histórico de migrações**

```powershell
docker-compose exec workout_api alembic history
```

### **Ver status atual**

```powershell
docker-compose exec workout_api alembic current
```

## 💻 **Opção 2: Ambiente Virtual Local**

### **Ativar ambiente virtual**

```powershell
# Navegar para pasta workoutapi
cd workoutapi

# Ativar ambiente
.\Scripts\Activate.ps1
```

### **Instalar dependências**

```powershell
pip install -r requirements.txt
```

### **Comandos Alembic locais**

```powershell
# Definir variável de ambiente para banco
$env:DATABASE_URL="postgresql://workout:workout@localhost:5432/workout"

# Criar migração
alembic revision --autogenerate -m "nome_da_migracao"

# Aplicar migrações
alembic upgrade head

# Ver histórico
alembic history
```

## 🔧 **Comandos de Exemplo Completos**

### **1. Primeira vez configurando**

```powershell
# Via Docker (mais fácil)
docker-compose exec workout_api alembic revision --autogenerate -m "create_atleta_table"
docker-compose exec workout_api alembic upgrade head
```

### **2. Adicionando nova tabela**

```powershell
# Criar migração
docker-compose exec workout_api alembic revision --autogenerate -m "add_categoria_table"

# Aplicar
docker-compose exec workout_api alembic upgrade head
```

### **3. Verificar se deu certo**

```powershell
# Ver tabelas criadas no banco
docker-compose exec workout_api_db psql -U workout -d workout -c "\dt"
```

## 🚨 **Erros Comuns e Soluções**

### **Erro: "else:" não é reconhecido**

❌ **Problema**: Tentando executar sintaxe Linux no PowerShell

```bash
# ERRADO no PowerShell
if [ condition ]; then
    command
else:
    other_command
fi
```

✅ **Solução**: Use os comandos do Docker ou PowerShell

```powershell
# CORRETO
docker-compose exec workout_api alembic upgrade head
```

### **Erro: PYTHONPATH não reconhecido**

❌ **Problema**:

```powershell
PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "migration"
```

✅ **Solução**:

```powershell
# Opção 1: Via Docker
docker-compose exec workout_api alembic revision --autogenerate -m "migration"

# Opção 2: PowerShell
$env:PYTHONPATH="$env:PYTHONPATH;$PWD"
alembic revision --autogenerate -m "migration"
```

## 📋 **Checklist de Verificação**

1. ✅ Containers rodando: `docker-compose ps`
2. ✅ Banco conectando: `docker-compose exec workout_api_db psql -U workout -d workout -c "SELECT version();"`
3. ✅ Alembic configurado: Arquivos criados ✅
4. ✅ Modelos importados: AtletaModel ✅

## 🎯 **Próximo Passo**

Execute este comando para criar as tabelas:

```powershell
docker-compose exec workout_api alembic revision --autogenerate -m "create_initial_tables"
```

Depois:

```powershell
docker-compose exec workout_api alembic upgrade head
```

## 🔍 **Verificar Resultado**

```powershell
# Ver tabelas criadas
docker-compose exec workout_api_db psql -U workout -d workout -c "\dt"

# Ver estrutura da tabela atletas
docker-compose exec workout_api_db psql -U workout -d workout -c "\d atletas"
```
