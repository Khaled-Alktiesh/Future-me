from firebase_config import get_db_ref  # ✅ Korrect Import

# Skriv testdata till Firebase.
test_ref = get_db_ref("test")
test_ref.set({"message": "Hello Firebase from Python!"})

# Läs tillbaka data från Firebase.
retrieved_data = test_ref.get()
print("✅ Firebase Test Success! Data Retrieved:", retrieved_data)