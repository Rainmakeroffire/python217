from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.orm import relationship
from models.database import Base


class Salesman(Base):
    __tablename__ = 'salesmen'
    sid = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(100), nullable=False)
    margin = Column(REAL, nullable=False)
    city = Column(String(100), nullable=False)
    _customers = relationship('Customer', back_populates='_salesman')

    def __repr__(self):
        return f'Salesperson ID: {self.sid}, ' \
               f'Name: {self.sname},' \
               f'Margin: {self.margin}' \
               f'City: {self.city}'
