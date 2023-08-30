import firebase_admin
from firebase_admin import credentials, storage, firestore


cred = credentials.Certificate('firebase_config.json')
storage_bucket = {
                    'storageBucket': 'colorextractor-df7b6.appspot.com'
                }

firebase_admin.initialize_app(cred, storage_bucket)

bucket = storage.bucket()
db = firestore.client()
