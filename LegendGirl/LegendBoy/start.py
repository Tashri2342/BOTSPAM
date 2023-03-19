from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos

@Client.on_message(filters.user(sudos) & filters.command(["start"], prefixes=HANDLER))
async def start(Legend: Client, message: Message):
    await Legend.send_photo(message.chat.id, ALIVE_PIC, caption="Hello")
