# ==============================================================================
# Workout API - Makefile
# ==============================================================================

.PHONY: help up down build rebuild logs shell db-shell create-migrations migrate rollback status clean

# Variables
DOCKER_COMPOSE = docker-compose
SERVICE_API = workout_api
SERVICE_DB = workout_api_db

# Default target
help: ## Show this help message
	@echo "Workout API - Available Commands:"
	@echo "================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Docker Commands
up: ## Start all services
	$(DOCKER_COMPOSE) up -d

down: ## Stop all services
	$(DOCKER_COMPOSE) down

build: ## Build the application
	$(DOCKER_COMPOSE) build $(SERVICE_API)

rebuild: ## Rebuild and restart services
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) build --no-cache $(SERVICE_API)
	$(DOCKER_COMPOSE) up -d

logs: ## Show application logs
	$(DOCKER_COMPOSE) logs -f $(SERVICE_API)

logs-db: ## Show database logs
	$(DOCKER_COMPOSE) logs -f $(SERVICE_DB)

status: ## Show services status
	$(DOCKER_COMPOSE) ps

# Application Commands
shell: ## Access application shell
	$(DOCKER_COMPOSE) exec $(SERVICE_API) bash

db-shell: ## Access database shell
	$(DOCKER_COMPOSE) exec $(SERVICE_DB) psql -U workout -d workout

# Database Migration Commands
create-migrations: ## Create new migration (usage: make create-migrations d="description")
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic revision --autogenerate -m "$(d)"

migrate: ## Apply migrations
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic upgrade head

rollback: ## Rollback last migration
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic downgrade -1

migration-status: ## Show migration status
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic current

migration-history: ## Show migration history
	$(DOCKER_COMPOSE) exec $(SERVICE_API) alembic history

# Database Commands
db-reset: ## Reset database (WARNING: deletes all data)
	$(DOCKER_COMPOSE) down -v
	$(DOCKER_COMPOSE) up -d
	@echo "Waiting for database to be ready..."
	@sleep 10
	make migrate

db-tables: ## Show database tables
	$(DOCKER_COMPOSE) exec $(SERVICE_DB) psql -U workout -d workout -c "\dt"

db-describe: ## Describe atletas table
	$(DOCKER_COMPOSE) exec $(SERVICE_DB) psql -U workout -d workout -c "\d atletas"

# Development Commands
install: ## Install development dependencies
	$(DOCKER_COMPOSE) exec $(SERVICE_API) pip install -r requirements.txt

test: ## Run tests
	$(DOCKER_COMPOSE) exec $(SERVICE_API) pytest

format: ## Format code with black
	$(DOCKER_COMPOSE) exec $(SERVICE_API) black workout_api/

lint: ## Lint code with flake8
	$(DOCKER_COMPOSE) exec $(SERVICE_API) flake8 workout_api/

# Utility Commands
clean: ## Clean up Docker resources
	docker system prune -f
	docker volume prune -f

clean-all: ## Clean up everything (WARNING: removes all Docker data)
	docker system prune -a -f
	docker volume prune -f

backup-db: ## Create database backup
	$(DOCKER_COMPOSE) exec $(SERVICE_DB) pg_dump -U workout workout > backup_$(shell date +%Y%m%d_%H%M%S).sql

# PgAdmin Commands
pgadmin-up: ## Start PgAdmin interface
	$(DOCKER_COMPOSE) --profile tools up -d
	@echo "PgAdmin available at: http://localhost:5050"
	@echo "Email: admin@workoutapi.com"
	@echo "Password: admin123"

pgadmin-down: ## Stop PgAdmin interface
	$(DOCKER_COMPOSE) --profile tools down

# API Testing
test-api: ## Test API endpoints
	@echo "Testing API endpoints..."
	@curl -s http://localhost:8000/ | jq .
	@echo "\nHealth check:"
	@curl -s http://localhost:8000/health | jq .

# Quick Setup
init: ## Initialize project (first time setup)
	@echo "Initializing Workout API..."
	make up
	@echo "Waiting for services to be ready..."
	@sleep 15
	make create-migrations d="initial_tables"
	make migrate
	@echo "✅ Project initialized successfully!"
	@echo "API: http://localhost:8000"
	@echo "Docs: http://localhost:8000/docs"

# Development workflow
dev: ## Start development environment
	make up
	make logs 