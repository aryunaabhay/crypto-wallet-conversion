### Instalación de dependencias
pip install fastapi uvicorn

### Levantar el servidor
uvicorn transaction_request_service.service:app --reload --host 0.0.0.0 --port 8000

Esto iniciará el servidor FastAPI y estará disponible en http://localhost:8000.

Interfaz de Documentación
Una vez que el servidor esté corriendo, podra acceder a las siguientes interfaces de documentación:

Swagger UI URL: http://localhost:8000/docs Aquí puedes explorar y probar los endpoints de manera interactiva.

ReDoc URL: http://localhost:8000/redoc Esta interfaz ofrece una visualización estructurada de los detalles de la API.
