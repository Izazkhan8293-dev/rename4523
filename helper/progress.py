import math, time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PROGRESS_BAR = """
{5}
Size    : {1} | {2}
Done    : {0}%
Speed   : {3}/s
ETA     : {4}
"""

def humanbytes(size):
    if not size: return ""
    power = 2**10; n=0; Dic_powerN={0:'B',1:'KB',2:'MB',3:'GB',4:'TB'}
    while size>power: size/=power;n+=1
    return f"{round(size,2)} {Dic_powerN[n]}"

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((f"{days}d, ") if days else "") + ((f"{hours}h, ") if hours else "") + ((f"{minutes}m, ") if minutes else "") + ((f"{seconds}s, ") if seconds else "") + ((f"{milliseconds}ms, ") if milliseconds else "")
    return tmp[:-2]

async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.0) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff > 0 else 0
        time_to_completion = round((total-current)/speed) if speed>0 else 0
        filled_blocks = math.floor(percentage/5)
        empty_blocks = 20-filled_blocks
        progress_bar = "■"*filled_blocks+"□"*empty_blocks
        tmp = PROGRESS_BAR.format(round(percentage,2), humanbytes(current), humanbytes(total), humanbytes(speed), TimeFormatter(time_to_completion*1000), progress_bar)
        cancel_btn = InlineKeyboardButton("✖️ Cancel", callback_data="cancel")
        try:
            await message.edit(text=f"{ud_type}\n\n{tmp}", reply_markup=InlineKeyboardMarkup([[cancel_btn]]))
        except: pass
