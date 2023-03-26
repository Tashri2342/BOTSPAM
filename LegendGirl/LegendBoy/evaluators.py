import asyncio
import os
import sys
from io import StringIO
from async_eval import eval
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos


# full debugging
@Client.on_message(filters.user(sudos) & filters.command(["eval"], prefixes=HANDLER))
async def pm(c: Client, m: Message):
  global c,m
  text = m.text[6:]
  try:
    vc = eval(text)
  except Exception as e:
    vc = str(e)
  try:
    await m.edit(f"Code : `{text}`\n\nResult : {str(vc)}",disable_web_page_preview=True,parse_mode=pyrogram.enums.ParseMode.MARKDOWN)
  except Exception as e:
   try:
    await m.edit(f"Code : `{text}`\n\nResult : {str(e)}",disable_web_page_preview=True,parse_mode=pyrogram.enums.ParseMode.MARKDOWN)
   except:
     pass
   with open("Result.txt" , "w") as g:
    g.writelines(str(vc))
    g.close()
   """x = (await app.get_chat_member(m.chat.id,(await app.get_me()).id)).status if (m.chat.type == ChatType.SUPERGROUP) else None
   if (x == ChatMemberStatus.MEMBER) or (x == ChatMemberStatus.RESTRICTED):
     return"""
   try:
     await m.reply_document("Result.txt")
   except:
     return


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
