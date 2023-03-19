from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos

handler = HANDLER
ALIVE_PIC = "https://te.legra.ph/file/315ec5fe03f2a612139b3.jpg"


@Client.on_message(filters.user(sudos) & filters.command(["start"], prefixes=handler))
async def start(Legend: Client, message: Message):
    await Legend.send_photo(message.chat.id, ALIVE_PIC, caption="Hello")
