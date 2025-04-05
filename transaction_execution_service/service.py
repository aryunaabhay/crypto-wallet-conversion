#Flask para crear el servidor, manejar peticiones y respuestas en JSON
from flask import Flask, request, jsonify
# Para ejecutar procesos los hilos
import threading
#simular delay o espera de tiemos
import time

app = Flask(__name__)

#simulacion de base de datos

transacciones=[
    {
     "id": 1,
        "moneda_origen": "USD",
        "moneda_destino": "EUR",
        "valor": 100,
        "estado": "no_procesada"
    },
    {
        "id": 2,
        "moneda_origen": "EUR",
        "moneda_destino": "JPY",
        "valor": 250,
        "estado": "no_procesada"
    }
]

#saber si el servidr esta activo

@app.route('/')
def home():
    return "servicio de transapcines activo"


#obtener transacciones

@app.route('/transacciones', methods=['GET'])
def obtener_transacciones():
    return jsonify(transacciones)

#actualizar el estado de transaccion

@app.route('/actualizar', methods=['POST'])
def actualizar():
    data = request.get_json()


    id_buscado = data.get("id")
    nuevo_estado= data.get("estado")

#Busqueda pr ID

    transaccion=next((t for t in transacciones if t["id"]== id_buscado),None)

#manejo de error por si la transacccion falla al buscarla

    if not transaccion: 
        return jsonify({"error": "la transaccion no fue encontrada"}),404


#actualiza  el estado con el valro del request

    transaccion["estado"] = nuevo_estado
    return jsonify({"mensaje": "Transacción actualizada", "transaccion": transaccion})


#loop para procesar las transacciones

def procesar_transacciones():
   
    while True:
        for transaccion in transacciones:
            if transaccion["estado"]=="no_procesada":
               transaccion["estado"]="en_proceso"
               print(f"transaccion en proceso {transaccion['id']}...")
            
            #simular un procesamiento o espera
               time.sleep(2)
               transaccion["estado"] = "procesada"
               print(f" Transacción {transaccion['id']} completada.")
        
        time.sleep(5)

        if all(t["estado"] == "procesada" for t in transacciones):
           print("Todas las transacciones fueron procesadas")
        break


#hilo para procesar las transacciones de manefa automatica

proceso_transacciones = threading.Thread(target=procesar_transacciones)
proceso_transacciones.daemon = True  #Se cierra si se apaga el servidor
proceso_transacciones.start() #iniciar proceso

if __name__ == '__main__':
    app.run(debug=True)
