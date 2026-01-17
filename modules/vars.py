import os

API_ID    = os.environ.get("API_ID", "20807000")
API_HASH  = os.environ.get("API_HASH", "cde2366a7c61e23f4cb44618cbe6cf70")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8564398983:AAHuuntq53gVgwIxQash63fatvHq-27BJTc") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
