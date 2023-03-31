import asyncio
from random import choice
from pyrogram.errors import FloodWait
from LegendBS.raid import RAID
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *
from ..core.clients import *
from .. import sudos

unlimited = False


@Client.on_message(filters.user(sudos) & filters.command(["uspam"], prefixes=HANDLER))
async def uspam(Legend: Client, message: Message):
    usage = f"Command : {HANDLER}uspam (message)"
    try:
        msg = str(e.text[6:])
    except IndexError:
        return await message.reply_text(usage)
    if message.reply_to_message:
        lmao = message.reply_to_message
        global unlimited 
        unlimited = True
        while unlimited == True:
            try:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(chat.id, f"{lmao.from_user.mention} {msg}")
            except FloodWait as op:
                print(op)
            return
    else:
        global unlimited 
        unlimited = True
        while unlimited == True:
            try:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(chat.id, msg)
            except FloodWait as op:
                print(op)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started Unlimited Spam \n\n• User: {e.from_user.id} \n• Chat: {e.chat.id} \n• Spam Message: {msg}",
            )
        except Exception as a:
            print(a)

"""
@Client.on_message(filters.user(sudos) & filters.command(["uraid"], prefixes=HANDLER))
async def uraid(Legend: Client, e: Message):
    global spam
    spam = True
    if e.reply_to_message:
        lmao = e.reply_to_message
        while spam == True:
            try:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(chat.id, f"{lmao.from_user.mention} {choice(RAID)}")
            except FloodWait as e:
                print(e)
            return
    else:
        while spam == True:
            try:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(chat.id, choice(RAID))
            except FloodWait as op:
                print(op)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["abuse", "gali"], prefixes=HANDLER)
)
async def _abuse(Legend: Client, e: Message):
    usage = f"Command :- {HANDLER}abuse (count)"
    msg = choice(RAID)
    if e.reply_to_message:
        while spam == True
            for i in range(1, 26):
                lol = global()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{reply.from_user.mention} {msg}")
            await asyncio.sleep(0.2)
    else:
        global spam
        spam = True
        try:
            while spam == True:
                for i in range(1, 26):
                    lol = global()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, msg)
                await asyncio.sleep(0.2)
        except FloodWait as ex:
            print(ex)
        

@Client.on_message(filters.user(sudos) & filters.command(["stop"], prefixes=HANDLER))
async def stop(_, e: Message):
    global spam
    spam = False
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
"""
