
async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import *

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@bot.on(events.NewMessage(pattern="/spam"))
@bot2.on(events.NewMessage(pattern="/spam"))
@bot3.on(events.NewMessage(pattern="/spam"))
@bot4.on(events.NewMessage(pattern="/spam"))
@bot5.on(events.NewMessage(pattern="/spam"))
@bot6.on(events.NewMessage(pattern="/spam"))
@bot7.on(events.NewMessage(pattern="/spam"))
@bot8.on(events.NewMessage(pattern="/spam"))
@bot9.on(events.NewMessage(pattern="/spam"))
@bot10.on(events.NewMessage(pattern="/spam"))
async def spam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(legend) == 2:
            message = str(legend[1])
            counter = int(legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(legend[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
