# WorkOut API

Uma API REST para gerenciar workouts e exercícios, desenvolvida com FastAPI.

## 🚀 Funcionalidades

- ✅ Criar, listar, atualizar e deletar workouts
- ✅ Filtrar workouts por nível de dificuldade
- ✅ Documentação automática com Swagger UI
- ✅ Validação de dados com Pydantic
- ✅ Estrutura modular e escalável

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI para produção
- **Python 3.8+**: Linguagem de programação

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd DIO-WORKOUT-API
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. Inicie o servidor:

```bash
python -m workout_api.main
```

2. Acesse a API em: `http://localhost:8000`

3. Acesse a documentação interativa:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## 📖 Endpoints da API

### Rotas Principais

- `GET /` - Página inicial da API
- `GET /health` - Verificação de saúde da API

### Workouts

- `GET /workouts/` - Listar todos os workouts
- `POST /workouts/` - Criar um novo workout
- `GET /workouts/{id}` - Obter workout específico
- `PUT /workouts/{id}` - Atualizar workout
- `DELETE /workouts/{id}` - Deletar workout
- `GET /workouts/difficulty/{level}` - Filtrar por dificuldade

### Exemplo de Workout

```json
{
  "name": "Treino de Força",
  "description": "Treino focado em exercícios de musculação",
  "duration_minutes": 60,
  "difficulty": "intermediate",
  "equipment": ["halteres", "barra", "banco"]
}
```

### Níveis de Dificuldade

- `beginner` - Iniciante
- `intermediate` - Intermediário
- `advanced` - Avançado

## 🧪 Testando a API

### Criar um Workout

```bash
curl -X POST "http://localhost:8000/workouts/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Treino HIIT",
    "description": "Treino intervalado de alta intensidade",
    "duration_minutes": 30,
    "difficulty": "advanced",
    "equipment": ["nenhum"]
  }'
```

### Listar Workouts

```bash
curl -X GET "http://localhost:8000/workouts/"
```

### Obter Workout por ID

```bash
curl -X GET "http://localhost:8000/workouts/1"
```

## 🏗️ Estrutura do Projeto

```
workout_api/
├── __init__.py
├── main.py              # Aplicação principal
└── routers/
    ├── __init__.py
    └── workout.py       # Rotas dos workouts
```

## 🔄 Próximos Passos

- [ ] Integração com banco de dados (SQLite/PostgreSQL)
- [ ] Sistema de autenticação e autorização
- [ ] Adicionar modelos para usuários e exercícios
- [ ] Implementar sistema de categorias
- [ ] Adicionar testes unitários
- [ ] Deploy em produção

## 📝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como parte do bootcamp DIO (Digital Innovation One).
