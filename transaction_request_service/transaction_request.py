from db import db


class TransactionRequest(db.Model):
    __tablename__ = 'transaction_requests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency_from = db.Column(db.String(4), nullable=False)
    currency_to = db.Column(db.String(4), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
