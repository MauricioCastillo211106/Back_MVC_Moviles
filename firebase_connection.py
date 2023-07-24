# firebase_connection.py
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from decouple import config
import os

firebase_credential_path = os.path.join(os.path.dirname(__file__), config("JSON_FIREBASE"))

# Inicializar la aplicación de Firebase con el nombre del bucket y el proyecto
initialize_app(credentials.Certificate(firebase_credential_path), {
    'storageBucket': config("BUCKET"),
    'projectId': config("PROJECT_ID")
})
# Obtén una referencia a la colección en Firestore
db_firestore = firestore.client()
