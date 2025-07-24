from __future__ import annotations
from typing import TYPE_CHECKING

from workout_api.contrib.models import BaseModel
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship, Mapped

if TYPE_CHECKING:
    from workout_api.atleta.models import AtletaModel



class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    nome = Column(String(100), unique=True, nullable=False)
    
    # Relationships
    atletas = relationship("AtletaModel", back_populates="categoria")
  