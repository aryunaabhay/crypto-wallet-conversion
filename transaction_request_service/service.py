from flask import request, jsonify
from transaction_request import TransactionRequest
from config import create_app
from db import db

app = create_app()


@app.route('/create_transaction_request', methods=['POST'])
def create_transaction_request():
    try:
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
        return jsonify({"id": transaction_request.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/get_transaction_status/<int:transaction_id>', methods=['GET'])
def get_transaction_status(transaction_id):
    try:
        transaction_request = TransactionRequest.query.get(transaction_id)
        if transaction_request:
            return jsonify({"id": transaction_request.id, "status": transaction_request.status}), 200
        else:
            return jsonify({"error": "Transaction not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500