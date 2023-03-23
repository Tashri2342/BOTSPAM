import asyncio
from random import choice

from LegendBS.banall import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos

@Client.on_message(filters.user(sudos) & filters.command(["raid"], prefixes=HANDLER))
async def banall(Legend: Client, message: Message):
   if message.chat.id == message.from_user.id:
     await message.reply_text("Use this CMD in group;")
     return
   await start_banall(Legend, message)

