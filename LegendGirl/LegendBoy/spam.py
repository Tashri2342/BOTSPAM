from LegendBoy.Config import *
from pyrogram import Client, filters
from pyrogram.types import *

from .. import sudos


@Client.on_message(
    filters.user(sudos) & filters.command(["spam", "bigspam"], prefixes=handler)
)
async def spam(Legend: Client, e: Message):
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(lol) == 2:
        counts = int(lol[0])
        spam_text = str(lol[1])
        chat = message.chat
        for _ in range(counts):
            await Legend.send_message(chat.id, str(spam_text))
            await asyncio.sleep(0.3)
    else:
        await e.reply_text(usage)
        return
    if LOGS_CHANNEL:
        try:
            await Legend.send_message(
                LOGS_CHANNEL,
                f"started Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)
