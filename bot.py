import os
import threading
import asyncio
from flask import Flask
from plugins.cb_data import app  # only import app
from pyrogram import idle


# Don't import individual handlers
# Just let plugins dict handle them

# Flask server for Render health check
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "✅ Rename-Bot is running!"

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

async def run_bot():
    await app.start()
    print("✅ Bot started successfully")
    await idle()
    await app.stop()


   

