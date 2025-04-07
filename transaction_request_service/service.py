from flask import request, jsonify
from transaction_request import TransactionRequest
from config import create_app
from db import db
from flask_restx import Api, fields, Resource

app = create_app()
api = Api(app, version='1.0', title='Crypto Wallet API',
    description='A simple Crypto wallet API',
)

ns = api.namespace('transaction_request', description='wallet transactions')

# Define models for request and response payloads
transaction_request_model = api.model('TransactionRequest', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'amount': fields.Float(required=True, description='Transaction amount'),
    'currency_from': fields.String(required=True, description='Currency to convert from (e.g., eurc)'),
    'currency_to': fields.String(required=True, description='Currency to convert to (e.g., eurc)'),
    'status': fields.String(description='Transaction status (pending | completed | failed)')
})

transaction_status_model = api.model('TransactionStatus', {
    'id': fields.Integer(description='Transaction ID'),
    'status': fields.String(description='Transaction status')
})

# Update the create_transaction_request endpoint
@ns.route('/create')
class CreateTransactionRequestResource(Resource):
    @api.expect(transaction_request_model, validate=True)
    @api.response(201, 'Transaction created successfully', model=transaction_status_model)
    @api.response(500, 'Internal server error')
    @api.doc(description='Create a new transaction request')
    def post(self):
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
            return {"id": transaction_request.id, "status": transaction_request.status}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

# Update the get_transaction_status endpoint
@ns.route('/get_status/<int:transaction_id>')
class GetTransactionStatusResource(Resource):
    @api.response(200, 'Transaction status retrieved successfully', model=transaction_status_model)
    @api.response(404, 'Transaction not found')
    @api.response(500, 'Internal server error')
    @api.doc(description='Get the status of a transaction by its ID')
    def get(self, transaction_id):
        try:
            transaction_request = TransactionRequest.query.get(transaction_id)
            if transaction_request:
                return {"id": transaction_request.id, "status": transaction_request.status}, 200
            else:
                return {"error": "Transaction not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500