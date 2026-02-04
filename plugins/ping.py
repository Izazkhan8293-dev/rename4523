from pyrogram import filters

async def ping_handler(client, message):
    await message.reply_text("🏓 Pong!")

# register dynamically in bot.py after creating app
# app.add_handler(ping_handler)
