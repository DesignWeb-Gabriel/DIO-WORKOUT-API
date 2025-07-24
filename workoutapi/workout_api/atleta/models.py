from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from workout_api.contrib.models import BaseModel
from sqlalchemy import DateTime, Float, ForeignKey, String, Column, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

if TYPE_CHECKING:
    from workout_api.categorias.models import CategoriaModel  




class AtletaModel(BaseModel):
    __tablename__ = "atletas"
    
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    categoria_id = Column(UUID(as_uuid=True), ForeignKey("categorias.id"), nullable=False)
    centro_treinamento_id = Column(UUID(as_uuid=True), ForeignKey("centro_treinamento.id"), nullable=False)
    
    # Relationships
    categoria = relationship("CategoriaModel", back_populates="atletas")
    centro_treinamento = relationship("CentroTreinamentoModel", back_populates="atletas")