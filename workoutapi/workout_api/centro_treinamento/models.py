from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from workout_api.contrib.models import BaseModel
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

if TYPE_CHECKING:
    from workout_api.atleta.models import AtletaModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centro_treinamento"
    
    nome = Column(String(100), unique=True, nullable=False)
    endereco = Column(String(100), nullable=False)
    proprietario = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    atletas = relationship("AtletaModel", back_populates="centro_treinamento")
  