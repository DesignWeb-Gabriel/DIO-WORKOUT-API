from workout_api.atleta.models import AtletaModel
from workout_api.contrib.models import BaseModel
from sqlalchemy import Mapped, String, mapped_column
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship


class CentroTreinamentoModel(BaseModel):
  __tablename__ = "centro_treinamento"
  pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nome: Mapped[str] = mapped_column(String(100), nullable=False)
  endereco: Mapped[str] = mapped_column(String(100), nullable=False)
  proprietario: Mapped[str] = mapped_column(String(100), nullable=False)
  atletas: Mapped[list[AtletaModel]] = relationship("AtletaModel", back_populates="centro_treinamento")
  