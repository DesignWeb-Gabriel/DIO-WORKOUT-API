from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel

from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

api_router = APIRouter()

@api_router.post(
    '/', 
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria_nome = atleta_in.categoria
    centro_treinamento_nome = atleta_in.centro_treinamento

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome))
    ).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'A categoria {categoria_nome} não foi encontrada.'
        )
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))
    ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'O centro de treinamento {centro_treinamento_nome} não foi encontrado.'
        )
    
    # Verificar se CPF já existe
    cpf_exists = (await db_session.execute(
        select(AtletaModel).filter_by(cpf=atleta_in.cpf))
    ).scalars().first()
    
    if cpf_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f'Já existe um atleta cadastrado com o CPF: {atleta_in.cpf}'
        )
    
    try:
        atleta_id = uuid4()
        atleta_model = AtletaModel(
            id=atleta_id,
            nome=atleta_in.nome,
            cpf=atleta_in.cpf,
            idade=atleta_in.idade,
            peso=atleta_in.peso,
            altura=atleta_in.altura,
            sexo=atleta_in.sexo,
            categoria_id=categoria.id,
            centro_treinamento_id=centro_treinamento.id,
            created_at=datetime.utcnow()
        )
        
        db_session.add(atleta_model)
        await db_session.commit()
        await db_session.refresh(atleta_model)
        
        # Carregar as relações para retornar
        atleta_with_relations = (await db_session.execute(
            select(AtletaModel)
            .filter_by(id=atleta_id)
        )).scalars().first()
        
        return AtletaOut(
            id=atleta_with_relations.id,
            nome=atleta_with_relations.nome,
            cpf=atleta_with_relations.cpf,
            idade=atleta_with_relations.idade,
            peso=atleta_with_relations.peso,
            altura=atleta_with_relations.altura,
            sexo=atleta_with_relations.sexo,
            created_at=atleta_with_relations.created_at,
            updated_at=atleta_with_relations.updated_at,
            categoria=categoria,
            centro_treinamento=centro_treinamento
        )
        
    except Exception as e:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='Ocorreu um erro ao inserir os dados no banco'
        )


@api_router.get(
    '/', 
    summary='Consultar todos os Atletas',
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas = (await db_session.execute(
        select(AtletaModel)
    )).scalars().all()
    
    result = []
    for atleta in atletas:
        # Buscar categoria e centro de treinamento
        categoria = (await db_session.execute(
            select(CategoriaModel).filter_by(id=atleta.categoria_id)
        )).scalars().first()
        
        centro_treinamento = (await db_session.execute(
            select(CentroTreinamentoModel).filter_by(id=atleta.centro_treinamento_id)
        )).scalars().first()
        
        result.append(AtletaOut(
            id=atleta.id,
            nome=atleta.nome,
            cpf=atleta.cpf,
            idade=atleta.idade,
            peso=atleta.peso,
            altura=atleta.altura,
            sexo=atleta.sexo,
            created_at=atleta.created_at,
            updated_at=atleta.updated_at,
            categoria=categoria,
            centro_treinamento=centro_treinamento
        ))
    
    return result


@api_router.get(
    '/{id}', 
    summary='Consulta um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    # Buscar categoria e centro de treinamento
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(id=atleta.categoria_id)
    )).scalars().first()
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(id=atleta.centro_treinamento_id)
    )).scalars().first()
    
    return AtletaOut(
        id=atleta.id,
        nome=atleta.nome,
        cpf=atleta.cpf,
        idade=atleta.idade,
        peso=atleta.peso,
        altura=atleta.altura,
        sexo=atleta.sexo,
        created_at=atleta.created_at,
        updated_at=atleta.updated_at,
        categoria=categoria,
        centro_treinamento=centro_treinamento
    )


@api_router.patch(
    '/{id}', 
    summary='Editar um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def patch(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    # Buscar categoria e centro de treinamento para retorno
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(id=atleta.categoria_id)
    )).scalars().first()
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(id=atleta.centro_treinamento_id)
    )).scalars().first()

    return AtletaOut(
        id=atleta.id,
        nome=atleta.nome,
        cpf=atleta.cpf,
        idade=atleta.idade,
        peso=atleta.peso,
        altura=atleta.altura,
        sexo=atleta.sexo,  
        created_at=atleta.created_at,
        updated_at=atleta.updated_at,
        categoria=categoria,
        centro_treinamento=centro_treinamento
    )


@api_router.delete(
    '/{id}', 
    summary='Deletar um Atleta pelo id',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    await db_session.delete(atleta)
    await db_session.commit()