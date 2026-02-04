import os
import asyncio
import threading
from flask import Flask
from pyrogram import idle
from plugins.cb_data import app  # session-based bot client

# ------------------ Flask Web Server ------------------
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "✅ Rename-Bot-4GB is running! - @JishuBotz"

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

# ------------------ Bot Main Loop ------------------
async def run_bot():
    await app.start()
    print("✅ Bot started successfully")
    await idle()
    await app.stop()

# ------------------ Entry Point ------------------
if __name__ == "__main__":
    # Start Flask server in a separate thread
    web_thread = threading.Thread(target=run_web)
    web_thread.start()

    # Start Pyrogram bot in async event loop
    asyncio.run(run_bot())
