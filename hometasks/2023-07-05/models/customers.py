from sqlalchemy import Column, ForeignKey, Integer, String, REAL
from sqlalchemy.orm import relationship
from models.database import Base


class Customer(Base):
    __tablename__ = 'customers'
    cid = Column(Integer, primary_key=True, autoincrement=True)
    cname = Column(String(100), nullable=False)
    rating = Column(REAL, nullable=False)
    city = Column(String(100), nullable=False)
    sid = Column(Integer, ForeignKey('salesmen.sid'))
    _salesman = relationship('Salesman', back_populates='_customers')

    def __repr__(self):
        return f'Customer ID: {self.cid}, ' \
               f'Name: {self.cname},' \
               f'Rating: {self.rating}' \
               f'City: {self.city}' \
               f'Manager ID: {self.sid}'
