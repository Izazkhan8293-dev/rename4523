import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")        # required now
STRING_SESSION = os.getenv("STRING_SESSION")  # optional, for 4GB uploads
ADMIN = int(os.getenv("ADMIN", 0))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
FORCE_SUBS = os.getenv("FORCE_SUBS", "")
START_PIC = os.getenv("START_PIC", "")
