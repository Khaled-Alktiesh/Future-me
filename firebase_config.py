import os
import firebase_admin
from firebase_admin import credentials, db

# 1. Define the path to the credentials file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this file
CREDENTIALS_PATH = os.path.join(BASE_DIR, "futureme-firebase-adminsdk.json")  # Path to the new credentials file

# 2. Check if the credentials file exists
if not os.path.exists(CREDENTIALS_PATH):
    raise FileNotFoundError(f"Credentials file not found at: {CREDENTIALS_PATH}")

# 3. Initialize Firebase Admin SDK
try:
    cred = credentials.Certificate(CREDENTIALS_PATH)  # Load credentials
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://console.firebase.google.com/project/future-me-13f5d/database/future-me-13f5d-default-rtdb/data/~2F"  # Replace with your new database URL
    })
    print("Firebase Admin SDK initialized successfully!")
except Exception as e:
    print(f"Failed to initialize Firebase: {e}")
    exit(1)

# 4. Function to get a reference to the database
def get_db_ref(path=""):
    return db.reference(path)