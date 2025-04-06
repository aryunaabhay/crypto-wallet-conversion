from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Define the Base class
Base = declarative_base()

class TransactionRequest(Base):
    __tablename__ = 'transaction_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    currency_from = Column(String(4), nullable=False)
    currency_to = Column(String(4), nullable=False)
    status = Column(String(20), nullable=False)
    
