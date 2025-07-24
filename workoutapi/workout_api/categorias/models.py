from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from workout_api.contrib.models import BaseModel
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import relationship, Mapped

if TYPE_CHECKING:
    from workout_api.atleta.models import AtletaModel



class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    nome = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    atletas = relationship("AtletaModel", back_populates="categoria")
  