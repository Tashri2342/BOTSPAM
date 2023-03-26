import asyncio
import os
import sys
from io import StringIO

from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos


# full debugging
@Client.on_message(filters.user(sudos) & filters.command(["eval"], prefixes=HANDLER))
async def eval(Legend: Client, message: Message):
    cmd = message.text[6:]
    if message.reply_to_message:
        code = message.reply_to_message.text.markdown
    elif cmd:
        try:
            code = message.text.split(" ", maxsplit=1)[1]
            if not code:
                return await message.reply_text("Gib me code!")
        except IndexError:
            code = message.text.split(" \n", maxsplit=1)[1]
            if not code:
                return await message.reply_text("Gib me code")
    else:
        return await message.reply_text("Gib me Code")
    result = sys.stdout = StringIO()
    try:
        lol = await eval("Your Result", code)
        await message.reply_text(
            f"<b>Code Try:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{lol}</code>"
        )
    except Exception as e:
        
        await message.reply_text(
            f"<b>Code Exception:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{sys.exc_info()[0].name}: {sys.exc_info()[1]}</code>"
        )


@Client.on_message(filters.user(sudos) & filters.command(["exec"], prefixes=HANDLER))
async def exec(Legend: Client, message: Message):
    cmd = message.text[6:]
    if message.reply_to_message:
        code = message.reply_to_message.text.markdown
    elif cmd:
        try:
            code = message.text.split(" ", maxsplit=1)[1]
            if not code:
                message.reply_text("Gib me code")
        except IndexError:
            code = message.text.split(" \n", maxsplit=1)[1]
            if not code:
                return await message.reply_text("Gib me code!")
    else:
        return await message.reply("Gib me execute code")
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    uid = os.geteuid()
    if uid == 0:
        await message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
    else:
        await message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
