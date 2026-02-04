from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.progress import progress_for_pyrogram
from config import *
import os
import asyncio
import time

# ------------------ Client ------------------
if STRING_SESSION:
    # optional session for future 4GB
    app = Client(
        name="my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION,
        plugins=dict(root="plugins")
    )
else:
    # normal bot token login for now
    app = Client(
        name="my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="plugins")
    )

# ------------------ /start ------------------
@app.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply_photo(
        photo=START_PIC or "",
        caption="👋 Hello! I am Rename-Bot.\nSend me a file to rename.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/JishuBotz")]])
    )

# ------------------ /rename ------------------
@app.on_message(filters.private & filters.document)
async def rename_file(bot, message):
    m = await message.reply_text("✏️ Send me the new file name (with extension):")
    try:
        response = await bot.listen(message.chat.id, timeout=60)
    except asyncio.TimeoutError:
        return await m.edit("⏰ Timeout! You took too long to send the new name.")

    new_file_name = response.text.strip()
    await m.edit("⚡ Downloading file...")

    start_time = time.time()
    file_path = await bot.download_media(
        message,
        file_name=new_file_name,
        progress=progress_for_pyrogram,
        progress_args=("Downloading...", m, start_time)
    )

    await m.edit("⚡ Uploading file...")
    await bot.send_document(
        chat_id=message.chat.id,
        document=file_path,
        caption=f"✅ Renamed to `{new_file_name}`",
        progress=progress_for_pyrogram,
        progress_args=("Uploading...", m, start_time)
    )

    try: os.remove(file_path)
    except: pass
    await m.delete()

# ------------------ Cancel ------------------
@app.on_callback_query(filters.regex("cancel"))
async def cancel(bot, update):
    await update.message.edit("❌ Operation Cancelled!")
