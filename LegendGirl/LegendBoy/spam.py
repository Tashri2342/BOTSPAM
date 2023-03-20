import asyncio

from pyrogram import Client, filters
from pyrogram.types import *

from LegendGirl.Config import *

from .. import sudos


@Client.on_message(
    filters.user(sudos) & filters.command(["spam", "bigspam"], prefixes=HANDLER)
)
async def spam(Legend: Client, e: Message):
    usage = "Command :- /spam <count> <text>\nExample :- `/spam 5 SpamBot OP`\n\n/bigspam <count> <text>\nExample :- `/bigspam 103 Legend Spam Bot`"
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(lol) == 2:
        counts = int(lol[0])
        spam_text = str(lol[1])
        chat = e.chat
        for _ in range(counts):
            await Legend.send_message(chat.id, str(spam_text))
    else:
        await e.reply_text(usage)
        return
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"started Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {spam_text}",
            )
        except Exception as a:
            print(a)
