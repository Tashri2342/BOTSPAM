from random import choice

from LegendBS.yup import *
from pyrogram import Client, filters
from pyrogram.types import *

from LegendGirl.Config import *

from .. import sudos
from ..core.clients import *

unlimited = False


@Client.on_message(filters.user(sudos) & filters.command(["shayri"], prefixes=HANDLER))
async def shayricmd(Legend: Client, e: Message):
    usage = f"Command: {HANDLER}shayri -u \nCommand:{HANDLER}shayri -u (reply to anyone)\nCommand: {HANDLER}shayri (count) \nCommand: {HANDLER}shayri (count) (reply to anyone)"
    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    flag = text[0]
    if not flag:
        return await e.reply_text(usage)
    shayrimsg = choice(shayrilol)
    if "-u" in flag:
        global unlimited
        unlimited = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            while unlimited == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{shayrimsg}"
                        )
        else:
            while unlimited == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, shayrimsg)
    elif "-u" not in flag:
        try:
            counts = int(text[0])
        except ValueError:
            return await e.reply_text(usage)
        if e.reply_to_message:
            lmao = e.reply_to_message
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{shayrimsg}"
                        )
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, shayrimsg)
    else:
        await e.reply_text(usage)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started Shayri Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["stopshayri"], prefixes=HANDLER)
)
async def stopwish(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("Stopped Unlimited Wish Shayri")
