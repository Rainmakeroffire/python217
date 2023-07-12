from sqlalchemy import Column, ForeignKey, Integer, DateTime
from models.database import Base


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    sid = Column(Integer, ForeignKey('salesmen.sid'))
    cid = Column(Integer, ForeignKey('customers.cid'))
    amount = Column(Integer)
    date = Column(DateTime)

    def __repr__(self):
        return f'Transaction ID: {self.id}, ' \
               f'Manager ID: {self.sid}, ' \
               f'Customer ID: {self.cid}, ' \
               f'Amount: {self.amount}, ' \
               f'Date: {self.date}'
