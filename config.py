import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
ADMIN = int(os.getenv("ADMIN", 0))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
