import firebase_admin
from firebase_admin import credentials, storage, firestore
from pathlib import Path

# Ruta absoluta de el archivo con los datos
json_path = Path(__file__).resolve().parent / 'data' / 'firebase_config.json'

cred = credentials.Certificate(json_path)
storage_bucket = {
                    'storageBucket': 'colorextractor-df7b6.appspot.com'
                }

firebase_admin.initialize_app(cred, storage_bucket)

bucket = storage.bucket()
db = firestore.client()
