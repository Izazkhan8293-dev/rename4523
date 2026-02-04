import os
import threading
import asyncio
from flask import Flask
from plugins.cb_data import client, app
from pyrogram import idle
from config import STRING_SESSION, API_ID, API_HASH, BOT_TOKEN

# Flask web server
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "✅ Rename-Bot is running! - @JishuBotz"

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

# Run Pyrogram bot
async def run_bot():
    await app.start()
    print("✅ Bot started successfully")
    await idle()
    await app.stop()

if STRING_SESSION:
    app = Client(
        name="my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION,
        plugins=dict(root="plugins")  # <-- must match your folder
    )
else:
    app = Client(
        name="my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="plugins")
    )
if __name__ == "__main__":
    # Start Flask in a separate thread
    threading.Thread(target=run_web, daemon=True).start()

    # Create a single event loop for the main thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())

