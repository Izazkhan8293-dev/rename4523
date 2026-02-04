from helper.progress import progress_for_pyrogram

async def download_file(bot, message, file_name, m, start_time):
    return await bot.download_media(
        message,
        file_name=file_name,
        progress=progress_for_pyrogram,
        progress_args=("Downloading...", m, start_time)
    )

async def upload_file(bot, chat_id, file_path, file_name, m, start_time, thumb=None):
    await bot.send_document(
        chat_id=chat_id,
        document=file_path,
        caption=f"✅ Renamed to `{file_name}`",
        thumb=thumb,
        progress=progress_for_pyrogram,
        progress_args=("Uploading...", m, start_time)
    )
