import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Fetch the service account key JSON file contents
cred = credentials.Certificate('')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

# As an admin, the app has access to read and write all data, regradless of Security Rules

def value():
    ref = db.reference("/1")
    return ref.get()["text_prompt"]
