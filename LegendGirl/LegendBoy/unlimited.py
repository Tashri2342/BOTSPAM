import asyncio
from random import choice

from LegendBS.get_user import user_only
from LegendBS.raid import RAID
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos

unlimited = False


@Client.on_message(filters.user(sudos) & filters.command(["uspam"], prefixes=HANDLER))
async def uspam(Legend: Client, e: Message):
    global unlimited
    unlimited = True
    msg = str(e.text[6:])
    if not msg:
        await e.reply("Gime Spam message bruh!")
        return
    try:
        while unlimited == True:
            await Legend.send_message(e.chat.id, msg)
    except Exception as ex:
        print(ex)
        await e.reply_text(f" Error -! \n\n {ex}")

    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"started Unlimited Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["uraid"], prefixes=HANDLER))
async def uraid(Legend: Client, e: Message):
    global unlimited
    unlimited = True
    user = await user_only(Legend, e)
    mention = user.mention
    try:
        while unlimited == True:
            choice(RAID)
            raid_msg = f"{mention} {reply}"
            await Legend.send_message(e.chat.id, raid_msg)
    except Exception as f:
        await e.reply_text(f" Error -! \n\n {f}")
        return

    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["abuse", "gali"], prefixes=HANDLER)
)
async def abuse(Legend: Client, e: Message):
    sex = e.text[7:]
    if sex:
        counts = int(sex)
        for _ in range(counts):
            msg = choice(one_word)
            await Legend.send_message(e.chat.id, msg)
            await asyncio.sleep(0.2)
    else:
        global unlimited
        unlimited = True
        try:
            while unlimited == True:
                msg = choice(RAID)
                await Legend.send_message(e.chat.id, msg)
        except Exception as ex:
            print(ex)
            await e.reply_text(f" Error -! \n\n {ex}")


@Client.on_message(filters.user(sudos) & filters.command(["stop"], prefixes=HANDLER))
async def stop(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")


@Client.on_message(
    filters.user(sudos) & filters.command(["echo", "repeat"], prefixes=HANDLER)
)
async def echo_(Legend: Client, message: Message):
    txt = " ".join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(
            f"**Wrong Usage!** \n\n Syntax: {HANDLER}echo (message or reply to message)"
        )
        return

    try:
        await message.delete()
        await Legend.send_message(message.chat.id, msg)
    except Exception as a:
        await Legend.send_message(message.chat.id, msg)
        print(str(a))
