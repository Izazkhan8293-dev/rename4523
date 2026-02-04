import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # optional if using bot token
ADMIN = int(os.getenv("ADMIN", 0))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
FORCE_SUBS = os.getenv("FORCE_SUBS", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "")
START_PIC = os.getenv("START_PIC", "")
