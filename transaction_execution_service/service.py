import sched
import time
from transaction_request import TransactionRequest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:Cryt0W4ll3t!@database:5432/crypto_wallet")
conn = engine.connect() 
Session = sessionmaker(bind=engine)
session = Session()

def get_last_transaction():
    last_transaction = (
        session.query(TransactionRequest)
        .filter_by(status="pending")
        .order_by(TransactionRequest.id.desc())
        .first()
    )
    if last_transaction:
        print("Last Transaction ID:", last_transaction.id)
    else:
        print("No pending transactions found.")

def run_periodically(scheduler, interval):
    get_last_transaction()
    scheduler.enter(interval, 1, run_periodically, (scheduler, interval))



scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, run_periodically, (scheduler, 2))
scheduler.run()