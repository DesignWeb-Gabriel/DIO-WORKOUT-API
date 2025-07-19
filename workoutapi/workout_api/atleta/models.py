from __future__ import annotations
import datetime
from typing import TYPE_CHECKING

from workout_api.contrib.models import BaseModel
from sqlalchemy import DateTime, Float, ForeignKey, String, Column, Integer
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from workout_api.categorias.models import CategoriaModel
    from workout_api.centro_treinamento.models import CentroTreinamentoModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"
    
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.pk_id"), nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"), nullable=False)
    
    # Relationships
    categoria = relationship("CategoriaModel", back_populates="atletas")
    centro_treinamento = relationship("CentroTreinamentoModel", back_populates="atletas")