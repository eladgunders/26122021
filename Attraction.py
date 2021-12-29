from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, REAL, Text, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base


class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name = Column(Text(), nullable=False)
    price = Column(REAL(), nullable=False)

    def __repr__(self):
        return f'Attraction(id={self.id}, name={self.name}, price={self.price})'

    def __str__(self):
        return f'Attraction[id={self.id}, name={self.name}, price={self.price}]'