from __future__ import annotations
from typing import TYPE_CHECKING

from workout_api.contrib.models import BaseModel
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship, Mapped

if TYPE_CHECKING:
    from workout_api.atleta.models import AtletaModel


class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True, nullable=False)
    
    # Relationships
    atletas = relationship("AtletaModel", back_populates="categoria")

    atleta: Mapped[list[AtletaModel]] = relationship(
        back_populates="categoria",
        cascade="all, delete-orphan",
    )
  