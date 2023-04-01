from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from LegendGirl.Config import *

from ..core.clients import *

from Data import Data

@Client.on_message(filters.command(["help"], prefixes=HANDLER))
async def help(Legend: Client, message: Message):
    HELP_MSG = "Help Menu Powered By @TeamLegendXD"
    if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
        await Legend.send_photo(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU),
        )
    elif ".mp4" in HELP_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU),
        )
    else:
        await Legend.send_message(message.chat_id, HELP_MSG , reply_markup=InlineKeyboardMarkup(Data.HELP_MENU))
