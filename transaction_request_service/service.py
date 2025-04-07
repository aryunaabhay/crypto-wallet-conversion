from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .db import db


from .transaction_request import TransactionRequest


app = FastAPI()

# Modelo para validación de datos de entrada
class TransactionRequestModel(BaseModel):
    user_id: int
    amount: float
    currency_from: str
    currency_to: str

@app.post("/create_transaction_request", status_code=201)
def create_transaction_request(request: TransactionRequestModel):
    try:
        transaction_request = TransactionRequest(
            user_id=request.user_id,
            amount=request.amount,
            currency_from=request.currency_from,
            currency_to=request.currency_to,
            status='pending'
        )
        db.session.add(transaction_request)
        db.session.commit()
        return {"id": transaction_request.id}
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_transaction_status/{transaction_id}")
def get_transaction_status(transaction_id: int):
    try:
        transaction_request = TransactionRequest.query.get(transaction_id)
        if transaction_request:
            return {"id": transaction_request.id, "status": transaction_request.status}
        else:
            raise HTTPException(status_code=404, detail="Transaction not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
