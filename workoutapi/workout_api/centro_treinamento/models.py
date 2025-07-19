from __future__ import annotations
from typing import TYPE_CHECKING

from workout_api.contrib.models import BaseModel
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from workout_api.atleta.models import AtletaModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centro_treinamento"
    
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True, nullable=False)
    endereco = Column(String(100), nullable=False)
    proprietario = Column(String(100), nullable=False)
    
    # Relationships
    atletas = relationship("AtletaModel", back_populates="centro_treinamento")
  