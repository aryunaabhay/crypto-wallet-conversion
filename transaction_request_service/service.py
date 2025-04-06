from flask import request, jsonify
from transaction_request import TransactionRequest
from config import create_app
from db import db

app = create_app()


@app.route('/create_transaction_request', methods=['POST'])
def create_transaction_request():
    data = request.get_json()
    transaction_request = TransactionRequest(
        user_id=data['user_id'],
        amount=data['amount'],
        currency_from=data['currency_from'],
        currency_to=data['currency_to'],
        status='pending'
    )
    db.session.add(transaction_request)
    db.session.commit()
    return jsonify({"message": "Transaction request created successfully!"}), 201

