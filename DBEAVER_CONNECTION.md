# 🗃️ DBeaver - Configuração de Conexão PostgreSQL

## 🔧 Configurações da Conexão

### **Aba Main:**

```
Server Host: localhost
Port: 5432
Database: workout_api
Username: workout_api
Password: workout_api_password
```

### **Aba PostgreSQL:**

- ✅ **Show all databases** (marcar)
- ❌ **Use SSL** (desmarcar)
- **Local Client**: Deixar padrão

### **Aba Driver properties:**

- **ApplicationName**: DBeaver
- **connectTimeout**: 30

## 🚨 Possíveis Problemas e Soluções

### 1. **Erro de SSL**

```
ATENÇÃO: Desmarque "Use SSL" na aba PostgreSQL
```

### 2. **Timeout de Conexão**

```
- Vá em Driver properties
- Altere connectTimeout para 30 ou 60
```

### 3. **Encoding/Charset**

```
- Vá em Driver properties
- Defina: characterEncoding = UTF8
```

### 4. **Porta ocupada**

```bash
# Verificar se a porta 5432 está livre
netstat -an | find "5432"
```

## ✅ Teste de Conectividade

### Via Terminal:

```bash
# Testar conexão direta
docker-compose exec workout_api_db psql -U workout_api -d workout_api -c "SELECT version();"
```

### Via DBeaver:

1. **Test Connection** antes de salvar
2. Se falhar, verificar logs detalhados
3. Tentar connection string manual

## 🌐 Connection String Alternativa

Se o método visual não funcionar, tente via connection string:

```
jdbc:postgresql://localhost:5432/workout_api?user=workout_api&password=workout_api_password&ssl=false
```

## 🔍 Debug Avançado

### Verificar containers:

```bash
docker-compose ps
docker-compose logs workout_api_db
```

### Testar conectividade de rede:

```bash
# Windows
telnet localhost 5432

# Ou via Docker
docker-compose exec workout_api_db pg_isready
```

## 📊 Após Conectar com Sucesso

Você deve ver:

- Database: `workout_api`
- Tables: ainda não criadas (será feito pelo Alembic)
- Schemas: `public`

## 🎯 Próximos Passos

1. ✅ **Conectar no DBeaver**
2. 🏗️ **Executar migrações** (Alembic)
3. 📋 **Visualizar tabelas criadas**
4. 🧪 **Testar API endpoints**

---

## 🆘 Se Ainda Não Funcionar

**Alternativa 1: Via pgAdmin**

```bash
docker-compose --profile tools up -d
# Acesse: http://localhost:5050
# Email: admin@workoutapi.com
# Senha: admin123
```

**Alternativa 2: Reset do banco**

```bash
docker-compose down -v
docker-compose up -d
```
