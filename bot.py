import os
import asyncio
import threading
from flask import Flask
from plugins.cb_data import app

# ------------------ Flask Web Server ------------------
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "✅ Rename-Bot is running! "

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

# ------------------ Bot Main Loop ------------------
async def run_bot():
    await app.start()
    print("✅ Bot started successfully")
    await asyncio.sleep(1)
    from pyrogram import idle
    await idle()
    await app.stop()

# ------------------ Entry Point ------------------
if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    asyncio.run(run_bot())
