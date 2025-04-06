from flask import Flask
from db import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cryt0W4ll3t!@database:5432/crypto_wallet'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app