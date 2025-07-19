# ==============================================================================
# Workout API - PowerShell Commands
# ==============================================================================

param(
    [string]$Command,
    [string]$d = ""
)

# Variables
$DockerCompose = "docker-compose"
$ServiceAPI = "workout_api"
$ServiceDB = "workout_api_db"

function Show-Help {
    Write-Host "Workout API - Available Commands:" -ForegroundColor Cyan
    Write-Host "=================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Docker Commands:" -ForegroundColor Yellow
    Write-Host "  up              Start all services"
    Write-Host "  down            Stop all services"
    Write-Host "  build           Build the application"
    Write-Host "  rebuild         Rebuild and restart services"
    Write-Host "  logs            Show application logs"
    Write-Host "  logs-db         Show database logs"
    Write-Host "  status          Show services status"
    Write-Host ""
    Write-Host "Application Commands:" -ForegroundColor Yellow
    Write-Host "  shell           Access application shell"
    Write-Host "  db-shell        Access database shell"
    Write-Host ""
    Write-Host "Database Migration Commands:" -ForegroundColor Yellow
    Write-Host "  create-migrations  Create new migration (use -d 'description')"
    Write-Host "  migrate            Apply migrations"
    Write-Host "  rollback           Rollback last migration"
    Write-Host "  migration-status   Show migration status"
    Write-Host "  migration-history  Show migration history"
    Write-Host ""
    Write-Host "Database Commands:" -ForegroundColor Yellow
    Write-Host "  db-reset        Reset database (WARNING: deletes all data)"
    Write-Host "  db-tables       Show database tables"
    Write-Host "  db-describe     Describe atletas table"
    Write-Host ""
    Write-Host "Development Commands:" -ForegroundColor Yellow
    Write-Host "  test            Run tests"
    Write-Host "  format          Format code with black"
    Write-Host "  lint            Lint code with flake8"
    Write-Host ""
    Write-Host "Utility Commands:" -ForegroundColor Yellow
    Write-Host "  clean           Clean up Docker resources"
    Write-Host "  backup-db       Create database backup"
    Write-Host "  pgadmin-up      Start PgAdmin interface"
    Write-Host "  pgadmin-down    Stop PgAdmin interface"
    Write-Host "  test-api        Test API endpoints"
    Write-Host "  init            Initialize project (first time setup)"
    Write-Host ""
    Write-Host "Usage Examples:" -ForegroundColor Green
    Write-Host "  .\commands.ps1 up"
    Write-Host "  .\commands.ps1 create-migrations -d 'add new table'"
    Write-Host "  .\commands.ps1 help"
}

function Start-Services {
    Write-Host "🚀 Starting all services..." -ForegroundColor Green
    & $DockerCompose up -d
}

function Stop-Services {
    Write-Host "⏹️ Stopping all services..." -ForegroundColor Yellow
    & $DockerCompose down
}

function Build-Application {
    Write-Host "🔨 Building application..." -ForegroundColor Blue
    & $DockerCompose build $ServiceAPI
}

function Rebuild-Services {
    Write-Host "🔄 Rebuilding and restarting services..." -ForegroundColor Magenta
    & $DockerCompose down
    & $DockerCompose build --no-cache $ServiceAPI
    & $DockerCompose up -d
}

function Show-Logs {
    Write-Host "📋 Showing application logs..." -ForegroundColor Cyan
    & $DockerCompose logs -f $ServiceAPI
}

function Show-DatabaseLogs {
    Write-Host "📋 Showing database logs..." -ForegroundColor Cyan
    & $DockerCompose logs -f $ServiceDB
}

function Show-Status {
    Write-Host "📊 Services status:" -ForegroundColor Cyan
    & $DockerCompose ps
}

function Enter-Shell {
    Write-Host "🐚 Accessing application shell..." -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI bash
}

function Enter-DatabaseShell {
    Write-Host "🗃️ Accessing database shell..." -ForegroundColor Green
    & $DockerCompose exec $ServiceDB psql -U workout -d workout
}

function Create-Migration {
    param([string]$Description)
    if (-not $Description) {
        Write-Host "❌ Error: Description is required. Use -d 'description'" -ForegroundColor Red
        return
    }
    Write-Host "📝 Creating new migration: $Description" -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI alembic revision --autogenerate -m $Description
}

function Apply-Migrations {
    Write-Host "⬆️ Applying migrations..." -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI alembic upgrade head
}

function Rollback-Migration {
    Write-Host "⬇️ Rolling back last migration..." -ForegroundColor Yellow
    & $DockerCompose exec $ServiceAPI alembic downgrade -1
}

function Show-MigrationStatus {
    Write-Host "📊 Current migration status:" -ForegroundColor Cyan
    & $DockerCompose exec $ServiceAPI alembic current
}

function Show-MigrationHistory {
    Write-Host "📜 Migration history:" -ForegroundColor Cyan
    & $DockerCompose exec $ServiceAPI alembic history
}

function Reset-Database {
    Write-Host "⚠️ WARNING: This will delete all data!" -ForegroundColor Red
    $confirmation = Read-Host "Are you sure? (y/N)"
    if ($confirmation -eq 'y' -or $confirmation -eq 'Y') {
        Write-Host "🔄 Resetting database..." -ForegroundColor Yellow
        & $DockerCompose down -v
        & $DockerCompose up -d
        Write-Host "⏳ Waiting for database to be ready..." -ForegroundColor Yellow
        Start-Sleep -Seconds 10
        Apply-Migrations
    } else {
        Write-Host "❌ Operation cancelled." -ForegroundColor Green
    }
}

function Show-DatabaseTables {
    Write-Host "📋 Database tables:" -ForegroundColor Cyan
    & $DockerCompose exec $ServiceDB psql -U workout -d workout -c "\dt"
}

function Describe-AtletasTable {
    Write-Host "📋 Atletas table structure:" -ForegroundColor Cyan
    & $DockerCompose exec $ServiceDB psql -U workout -d workout -c "\d atletas"
}

function Run-Tests {
    Write-Host "🧪 Running tests..." -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI pytest
}

function Format-Code {
    Write-Host "✨ Formatting code with black..." -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI black workout_api/
}

function Lint-Code {
    Write-Host "🔍 Linting code with flake8..." -ForegroundColor Green
    & $DockerCompose exec $ServiceAPI flake8 workout_api/
}

function Clean-Docker {
    Write-Host "🧹 Cleaning up Docker resources..." -ForegroundColor Yellow
    docker system prune -f
    docker volume prune -f
}

function Backup-Database {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupFile = "backup_$timestamp.sql"
    Write-Host "💾 Creating database backup: $backupFile" -ForegroundColor Green
    & $DockerCompose exec $ServiceDB pg_dump -U workout workout > $backupFile
    Write-Host "✅ Backup created: $backupFile" -ForegroundColor Green
}

function Start-PgAdmin {
    Write-Host "🚀 Starting PgAdmin..." -ForegroundColor Green
    & $DockerCompose --profile tools up -d
    Write-Host "🌐 PgAdmin available at: http://localhost:5050" -ForegroundColor Cyan
    Write-Host "📧 Email: admin@workoutapi.com" -ForegroundColor Yellow
    Write-Host "🔑 Password: admin123" -ForegroundColor Yellow
}

function Stop-PgAdmin {
    Write-Host "⏹️ Stopping PgAdmin..." -ForegroundColor Yellow
    & $DockerCompose --profile tools down
}

function Test-API {
    Write-Host "🧪 Testing API endpoints..." -ForegroundColor Green
    Write-Host "📍 Root endpoint:" -ForegroundColor Yellow
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/" -Method Get
        $response | ConvertTo-Json -Depth 2
    } catch {
        Write-Host "❌ API not responding" -ForegroundColor Red
    }
    
    Write-Host "`n🏥 Health check:" -ForegroundColor Yellow
    try {
        $health = Invoke-RestMethod -Uri "http://localhost:8000/health" -Method Get
        $health | ConvertTo-Json -Depth 2
    } catch {
        Write-Host "❌ Health check failed" -ForegroundColor Red
    }
}

function Initialize-Project {
    Write-Host "🚀 Initializing Workout API..." -ForegroundColor Green
    Start-Services
    Write-Host "⏳ Waiting for services to be ready..." -ForegroundColor Yellow
    Start-Sleep -Seconds 15
    Create-Migration -Description "initial_tables"
    Apply-Migrations
    Write-Host "✅ Project initialized successfully!" -ForegroundColor Green
    Write-Host "🌐 API: http://localhost:8000" -ForegroundColor Cyan
    Write-Host "📚 Docs: http://localhost:8000/docs" -ForegroundColor Cyan
}

# Main switch
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "up" { Start-Services }
    "down" { Stop-Services }
    "build" { Build-Application }
    "rebuild" { Rebuild-Services }
    "logs" { Show-Logs }
    "logs-db" { Show-DatabaseLogs }
    "status" { Show-Status }
    "shell" { Enter-Shell }
    "db-shell" { Enter-DatabaseShell }
    "create-migrations" { Create-Migration -Description $d }
    "migrate" { Apply-Migrations }
    "rollback" { Rollback-Migration }
    "migration-status" { Show-MigrationStatus }
    "migration-history" { Show-MigrationHistory }
    "db-reset" { Reset-Database }
    "db-tables" { Show-DatabaseTables }
    "db-describe" { Describe-AtletasTable }
    "test" { Run-Tests }
    "format" { Format-Code }
    "lint" { Lint-Code }
    "clean" { Clean-Docker }
    "backup-db" { Backup-Database }
    "pgadmin-up" { Start-PgAdmin }
    "pgadmin-down" { Stop-PgAdmin }
    "test-api" { Test-API }
    "init" { Initialize-Project }
    default { 
        if ([string]::IsNullOrEmpty($Command)) {
            Show-Help
        } else {
            Write-Host "❌ Unknown command: $Command" -ForegroundColor Red
            Write-Host "Use '.\commands.ps1 help' to see available commands" -ForegroundColor Yellow
        }
    }
} 