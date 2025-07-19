# 🪟 Windows Setup - Instalação do Make e Ferramentas

## 🚀 Opções para usar Make no Windows

### **Opção 1: Script PowerShell (Recomendado - Já Pronto)**

Use o arquivo `commands.ps1` que criamos:

```powershell
# Ver todos os comandos disponíveis
.\commands.ps1 help

# Exemplo de uso - criar migração
.\commands.ps1 create-migrations -d "init_db"

# Iniciar aplicação
.\commands.ps1 up

# Ver status
.\commands.ps1 status
```

### **Opção 2: Instalar Make no Windows**

#### **Via Chocolatey (Recomendado)**

1. **Instalar Chocolatey** (se não tiver):

   ```powershell
   # Executar como Administrador
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. **Instalar Make**:

   ```powershell
   # Executar como Administrador
   choco install make
   ```

3. **Usar Makefile**:
   ```bash
   # Após instalar, use normalmente
   make help
   make create-migrations d="init_db"
   make up
   ```

#### **Via Git Bash**

Se você tem Git instalado, pode usar o Git Bash:

1. **Abrir Git Bash** no diretório do projeto
2. **Usar comandos Make normalmente**:
   ```bash
   make help
   make create-migrations d="init_db"
   make up
   ```

#### **Via WSL (Windows Subsystem for Linux)**

1. **Instalar WSL**:

   ```powershell
   # Executar como Administrador
   wsl --install
   ```

2. **No terminal Ubuntu/WSL**:
   ```bash
   # Make já vem instalado
   make help
   make create-migrations d="init_db"
   ```

### **Opção 3: Usando Docker Desktop Terminal**

Docker Desktop inclui um terminal Linux integrado:

1. **Abrir Docker Desktop**
2. **Usar terminal integrado**
3. **Comandos funcionam normalmente**

---

## 📋 Comparação dos Métodos

| Método                | Prós                                                                      | Contras                                      | Recomendação                |
| --------------------- | ------------------------------------------------------------------------- | -------------------------------------------- | --------------------------- |
| **PowerShell Script** | ✅ Funciona nativamente<br/>✅ Colorido e intuitivo<br/>✅ Já configurado | ❌ Sintaxe diferente                         | ⭐ **Melhor para Windows**  |
| **Chocolatey + Make** | ✅ Sintaxe padrão<br/>✅ Portável                                         | ❌ Requer instalação<br/>❌ Permissões admin | ⚡ **Boa opção**            |
| **Git Bash**          | ✅ Sintaxe padrão<br/>✅ Sem instalação extra                             | ❌ Terminal separado                         | 🔧 **Para usuários Git**    |
| **WSL**               | ✅ Linux completo<br/>✅ Melhor performance                               | ❌ Setup mais complexo                       | 💻 **Para desenvolvedores** |

---

## 🎯 Comandos Equivalentes

### **Comando que você tentou usar:**

```powershell
# ❌ Não funcionava
make create-migrations d="init_db"
```

### **Soluções:**

#### **PowerShell (Recomendado):**

```powershell
# ✅ Funciona no Windows
.\commands.ps1 create-migrations -d "init_db"
```

#### **Make (após instalação):**

```bash
# ✅ Funciona com make instalado
make create-migrations d="init_db"
```

#### **Docker direto:**

```powershell
# ✅ Sempre funciona
docker-compose exec workout_api alembic revision --autogenerate -m "init_db"
```

---

## 🚀 Guia de Uso Rápido

### **PowerShell Script (Recomendado)**

```powershell
# 1. Ver comandos disponíveis
.\commands.ps1 help

# 2. Inicializar projeto (primeira vez)
.\commands.ps1 init

# 3. Comandos do dia a dia
.\commands.ps1 up                    # Iniciar
.\commands.ps1 logs                  # Ver logs
.\commands.ps1 status               # Status
.\commands.ps1 db-tables            # Ver tabelas
.\commands.ps1 create-migrations -d "nova_tabela"  # Nova migração
.\commands.ps1 migrate              # Aplicar migração
.\commands.ps1 down                 # Parar

# 4. Desenvolvimento
.\commands.ps1 test                 # Testes
.\commands.ps1 format               # Formatar código
.\commands.ps1 shell                # Acessar container

# 5. Banco de dados
.\commands.ps1 db-shell             # Acessar PostgreSQL
.\commands.ps1 pgadmin-up           # Abrir PgAdmin
.\commands.ps1 backup-db            # Backup
```

### **Makefile (se instalado)**

```bash
# 1. Ver comandos
make help

# 2. Inicializar projeto
make init

# 3. Comandos do dia a dia
make up
make logs
make status
make create-migrations d="nova_tabela"
make migrate

# 4. Desenvolvimento
make test
make format
make shell
```

---

## ✅ Teste de Funcionamento

### **Testar PowerShell Script:**

```powershell
# Deve mostrar menu de ajuda
.\commands.ps1 help

# Deve mostrar status dos containers
.\commands.ps1 status
```

### **Testar Make (se instalado):**

```bash
# Deve mostrar menu de ajuda
make help

# Deve mostrar versão
make --version
```

---

## 🛠️ Resolução de Problemas

### **PowerShell: Execution Policy**

```powershell
# Se der erro de política de execução
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Make: Comando não encontrado**

```powershell
# Verificar se está instalado
where make

# Se não estiver, escolher uma das opções de instalação acima
```

### **Docker: Não está rodando**

```powershell
# Iniciar Docker Desktop manualmente
# Aguardar aparecer "Docker Desktop is running"
```

---

## 🎯 Recomendação Final

Para **Windows**, recomendo usar o **`commands.ps1`**:

1. ✅ **Funciona nativamente** no PowerShell
2. ✅ **Interface colorida** e amigável
3. ✅ **Validações automáticas** (confirmações, erros)
4. ✅ **Já está configurado** e pronto para uso
5. ✅ **Mesma funcionalidade** do Makefile

```powershell
# Seu comando original equivalente:
.\commands.ps1 create-migrations -d "init_db"
```

🚀 **Agora você tem todas as ferramentas para trabalhar profissionalmente com a Workout API no Windows!**
