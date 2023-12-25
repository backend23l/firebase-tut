import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('/Users/djumanov/Desktop/private-key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection("cities").stream()

for doc in docs.limit(1):
    print(f"{doc.id} => {doc.to_dict()}")
