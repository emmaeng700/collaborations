import firebase_admin
from firebase_admin import credentials, firestore

# TODO (Akontoke): Initialize Firebase Admin SDK
# Save diagnosis results per user to Firestore collection: "scans"

def save_diagnosis(user_id: str, result: dict):
    # db = firestore.client()
    # db.collection("scans").add({**result, "user_id": user_id})
    pass

def get_user_history(user_id: str) -> list:
    # db = firestore.client()
    # docs = db.collection("scans").where("user_id", "==", user_id).stream()
    # return [d.to_dict() for d in docs]
    return []
