# 🗃️ DBeaver - Configuração de Conexão PostgreSQL

## 🎯 Conexão Rápida - Credenciais Atualizadas

### **📋 Dados de Conexão (Corretos)**

```
Host: localhost
Port: 5432
Database: workout
Username: workout
Password: workout
SSL: ❌ DESABILITADO (IMPORTANTE!)
```

---

## 🔧 Passo a Passo Detalhado

### **1. Criar Nova Conexão**

1. Abrir DBeaver
2. **Nova Conexão** → **PostgreSQL**
3. Clicar em **Next**

### **2. Aba "Principal" - Configurações Básicas**

```
Server Host: localhost
Port: 5432
Database: workout
Username: workout
Password: workout
☑️ Save password locally (opcional)
☑️ Show all databases (recomendado)
```

### **3. ⚠️ CRÍTICO - Aba "PostgreSQL"**

**Esta é a etapa mais importante:**

- ❌ **DESMARCAR "Use SSL"**
- ✅ **MARCAR "Show all databases"**
- **Local Client**: Deixar padrão

### **4. Aba "Driver properties" (Opcional)**

```
ApplicationName: DBeaver
connectTimeout: 30
characterEncoding: UTF8
```

### **5. Testar e Finalizar**

1. **Clicar "Test Connection"**
2. ✅ Deve aparecer: "Connected"
3. **Clicar "Finish"**

---

## ✅ Status Esperado Após Conexão

### **Databases Visíveis:**

- `workout` (database principal)
- `postgres` (database padrão)
- `template0`, `template1` (templates)

### **Tabelas no Database "workout":**

- ✅ `atletas` - Dados dos atletas
- ✅ `categorias` - Categorias esportivas
- ✅ `centro_treinamento` - Centros de treinamento
- ✅ `alembic_version` - Controle de migrações

### **Estrutura da Tabela "atletas":**

```sql
pk_id                 | integer     | PK, NOT NULL, AUTO_INCREMENT
nome                  | varchar(100)| NOT NULL
cpf                   | varchar(11) | UNIQUE, NOT NULL
idade                 | integer     | NOT NULL
peso                  | float       | NOT NULL
altura                | float       | NOT NULL
sexo                  | varchar(1)  | NOT NULL
created_at            | timestamp   | NOT NULL
categoria_id          | integer     | FK → categorias.pk_id
centro_treinamento_id | integer     | FK → centro_treinamento.pk_id
id                    | uuid        | NOT NULL
```

---

## 🚨 Problemas Comuns e Soluções

### **❌ Erro: "Authentication failed"**

**Causa:** SSL habilitado ou credenciais incorretas

```
Solução:
1. ⚠️ DESMARCAR "Use SSL" na aba PostgreSQL
2. Verificar credenciais: workout / workout
3. Testar novamente
```

### **❌ Erro: "Connection refused"**

**Causa:** Docker não está rodando

```
Solução:
1. Verificar containers: docker-compose ps
2. Iniciar se necessário: .\commands.ps1 up
3. Aguardar containers ficarem "healthy"
```

### **❌ Erro: "Database does not exist"**

**Causa:** Migrações não foram aplicadas

```
Solução:
1. Aplicar migrações: .\commands.ps1 migrate
2. Verificar tabelas: .\commands.ps1 db-tables
3. Reconectar no DBeaver
```

### **❌ Erro: "SSL connection required"**

**Causa:** PostgreSQL configurado para exigir SSL

```
Solução:
1. Na aba PostgreSQL: DESMARCAR "Use SSL"
2. Ou usar connection string: postgresql://workout:workout@localhost:5432/workout?sslmode=disable
```

---

## 🌐 Connection String Alternativa

Se a configuração visual não funcionar:

### **JDBC URL:**

```
jdbc:postgresql://localhost:5432/workout?user=workout&password=workout&ssl=false
```

### **PostgreSQL URL:**

```
postgresql://workout:workout@localhost:5432/workout?sslmode=disable
```

---

## 🔍 Verificação e Debug

### **1. Teste via Terminal (Antes do DBeaver)**

```powershell
# Verificar se containers estão rodando
.\commands.ps1 status

# Testar conexão direta
.\commands.ps1 db-shell

# Ver tabelas (dentro do PostgreSQL)
\dt

# Sair do PostgreSQL
\q
```

### **2. Comandos de Debug**

```powershell
# Ver logs do banco
.\commands.ps1 logs-db

# Verificar rede
netstat -an | findstr 5432

# Testar conectividade
telnet localhost 5432
```

### **3. Validação no DBeaver**

Após conectar com sucesso, execute:

```sql
-- Ver versão do PostgreSQL
SELECT version();

-- Contar registros em cada tabela
SELECT 'atletas' as tabela, COUNT(*) FROM atletas
UNION ALL
SELECT 'categorias', COUNT(*) FROM categorias
UNION ALL
SELECT 'centro_treinamento', COUNT(*) FROM centro_treinamento;

-- Ver estrutura da tabela atletas
\d atletas
```

---

## 🆘 Alternativas se DBeaver não Funcionar

### **1. PgAdmin via Docker**

```powershell
# Iniciar PgAdmin
.\commands.ps1 pgadmin-up

# Acessar: http://localhost:5050
# Email: admin@workoutapi.com
# Senha: admin123
```

### **2. Terminal PostgreSQL**

```powershell
# Acesso direto ao banco
.\commands.ps1 db-shell

# Comandos básicos:
\l          # Listar databases
\c workout  # Conectar ao database workout
\dt         # Listar tabelas
\d atletas  # Descrever tabela atletas
```

### **3. Extensão VSCode**

- **PostgreSQL** extension
- **Database Client** extension
- Usar mesmas credenciais

---

## 📊 Após Conexão Bem-Sucedida

### **Operações Recomendadas:**

1. **Explorar estrutura**: Expandir tabelas e ver colunas
2. **Testar consultas**: `SELECT * FROM atletas LIMIT 10;`
3. **Verificar relacionamentos**: Foreign keys funcionando
4. **Configurar favoritos**: Salvar queries frequentes

### **Queries Úteis:**

```sql
-- Ver todas as tabelas e seus tamanhos
SELECT
    schemaname,
    tablename,
    attname,
    typename,
    attlen,
    atttypmod,
    attnotnull,
    atthasdef
FROM pg_attribute, pg_class, pg_type, pg_namespace
WHERE relkind = 'r'
AND attnum > 0
AND schemaname = 'public';

-- Ver foreign keys
SELECT
    tc.table_schema,
    tc.constraint_name,
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE constraint_type = 'FOREIGN KEY';
```

---

## 🎯 Resumo - Checklist de Conexão

- [ ] ✅ Docker containers rodando (`.\commands.ps1 status`)
- [ ] ✅ Credenciais corretas (workout/workout)
- [ ] ❌ **SSL DESABILITADO** (mais importante!)
- [ ] ✅ Host: localhost, Port: 5432
- [ ] ✅ Database: workout
- [ ] ✅ Test Connection passou
- [ ] ✅ Tabelas visíveis (atletas, categorias, centro_treinamento)

**🏆 Com essas configurações, a conexão DBeaver funcionará perfeitamente!**
