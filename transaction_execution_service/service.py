import sched
import time
from transaction_request import TransactionRequest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#configuracion de bd

engine = create_engine("postgresql://postgres:Cryt0W4ll3t!@database:5432/crypto_wallet")
conn = engine.connect() 
Session = sessionmaker(bind=engine)
session = Session()




#simulacion de tasa de cambio entre monedas 

tasas = {
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1.08,
    ("USD", "JPY"): 150.0,
    ("JPY", "USD"): 0.0067,
    ("EUR", "JPY"): 163.0,
    ("JPY", "EUR"): 0.0061
}

#obtener la tasa segun origen y destino
def obtener_tasa(origen, destino):
    return tasas.get((origen, destino))

#procesamiento y conversion 

def procesar_transaccion(transaccion):

    try:
        transaccion.status = "processing"  #Cambia estado a "processing"
        session.commit()

        time.sleep(2)
        tasa = obtener_tasa(transaccion.currency_from, transaccion.currency_to)
        if tasa is None:
            print(f"Tasa no encontrada para {transaccion.currency_from} -> {transaccion.currency_to}")
            transaccion.status = "failed"  # Si no hay tasa, falla
            session.commit()
            return
#para calcular el monto 
        monto_convertido=transaccion.amount * tasa
        transaccion.status = "processed"
        session.commit()
        
        print(f"Transacción {transaccion.id} procesada: {transaccion.amount} {transaccion.currency_from} -> {monto_convertido:.2f} {transaccion.currency_to}")

#si hay exepcion marca falla
        
    except Exception as e:
        session.rollback()
        print(f"Error al procesar transacción {transaccion.id}: {e}")
        transaccion.status = "failed"  
        session.commit()

def get_last_transaction():
     return (
        session.query(TransactionRequest)
        .filter_by(status="pending")
        .order_by(TransactionRequest.id.asc())
        .first()
    )

def run_periodically(scheduler, interval):
    transaccion = get_last_transaction()
    if (transaccion):
        procesar_transaccion(transaccion)
    else: 
        print("sin transacciones ppendientes")
    scheduler.enter(interval, 1, run_periodically, (scheduler, interval))



scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, run_periodically, (scheduler, 2))
scheduler.run()