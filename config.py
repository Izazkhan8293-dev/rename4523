import os

API_ID = int(os.getenv("API_ID", "7839182"))
API_HASH = os.getenv("API_HASH", "c4787b79c1bc855dbcb6d7f84be81883")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7371314077:AAFZps8nn9KtqbbVn6LR7ztn9L-ZD5tcOak")        # required now
STRING_SESSION = os.getenv("STRING_SESSION", "")  # optional, for 4GB uploads
ADMIN = int(os.getenv("ADMIN", "1430259940"))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001685382274"))
FORCE_SUBS = os.getenv("FORCE_SUBS", "-1001685382274")
START_PIC = os.getenv("START_PIC", "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg")
