import os

API_ID = int(os.getenv("API_ID", "7839182"))
API_HASH = os.getenv("API_HASH", "c4787b79c1bc855dbcb6d7f84be81883")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7371314077:AAGMWMl3C8aHoXxqQ-BpHoX7ojbX4ISqEnc")        # required now
STRING_SESSION = os.getenv("STRING_SESSION")  # optional, for 4GB uploads
ADMIN = int(os.getenv("ADMIN", 1430259940))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1001685382274))
FORCE_SUBS = os.getenv("FORCE_SUBS", "-1001685382274")
START_PIC = os.getenv("START_PIC", "")
