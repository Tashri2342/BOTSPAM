from LegendBS.start import start_cmd
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from LegendGirl.Config import *


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def start(Legend: Client, message: Message):
    if ".jpg" in START_PIC or ".png" in START_PIC:
        await Legend.send_photo(
            message.chat.id,
            START_PIC,
            caption=ALIVE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
        )
    elif ".mp4" in START_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            START_PIC,
            caption=ALIVE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
        )
    else:
        await Legend.send_message(message.chat_id, ALIVE_MESSAGE)
