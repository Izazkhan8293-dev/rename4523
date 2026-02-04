from pyrogram import filters

@app.on_message(filters.private & filters.command("ping"))
async def ping(bot, message):
    await message.reply_text("Pong!")
