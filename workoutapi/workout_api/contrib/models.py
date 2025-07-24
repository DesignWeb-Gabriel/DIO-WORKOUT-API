from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID 

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)

