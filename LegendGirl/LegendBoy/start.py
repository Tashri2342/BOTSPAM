from pyrogram import Client, filters

from LegendGirl.Config import *

handler = HANDLER


@Client.on_message(filters.me & filters.command(["start"], prefixes=handler))
async def start(Legend: Client, message: Message):
    await Legend.send_message(message.chat.id, "Hello")