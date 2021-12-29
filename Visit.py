from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, REAL, Text, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(BigInteger(), primary_key=True)
    tourist_id = Column(BigInteger(), ForeignKey('tourists.id'), nullable=True)
    attraction_id = Column(BigInteger(), ForeignKey('attractions.id'), nullable=True)

    tourist = relationship('Tourist', backref=backref('visits', uselist=True))
    attraction = relationship('Attraction', backref=backref('visits', uselist=True))

    def __repr__(self):
        return f'Visit(id={self.id}, tourist_id={self.tourist_id}, attraction_id={self.attraction_id})'

    def __str__(self):
        return f'Visit(id={self.id}, tourist_id={self.tourist_id}, attraction_id={self.attraction_id})'