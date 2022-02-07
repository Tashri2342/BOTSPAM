
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import *
SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}



@bot.on(events.NewMessage(pattern="/raid"))
@bot2.on(events.NewMessage(pattern="/raid"))
@bot3.on(events.NewMessage(pattern="/raid"))
@bot4.on(events.NewMessage(pattern="/raid"))
@bot5.on(events.NewMessage(pattern="/raid"))
@bot6.on(events.NewMessage(pattern="/raid"))
@bot7.on(events.NewMessage(pattern="/raid"))
@bot8.on(events.NewMessage(pattern="/raid"))
@bot9.on(events.NewMessage(pattern="/raid"))
@bot10.on(events.NewMessage(pattern="/raid"))
async def spam(e):  
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        legendgirl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(legendgirl) == 2:
            message = str(legendgirl[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(legendgirl[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(legendgirl[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@bot.on(events.NewMessage(incoming=True))
@bot2.on(events.NewMessage(incoming=True))
@bot3.on(events.NewMessage(incoming=True))
@bot4.on(events.NewMessage(incoming=True))
@bot5.on(events.NewMessage(incoming=True))
@bot6.on(events.NewMessage(incoming=True))
@bot7.on(events.NewMessage(incoming=True))
@bot8.on(events.NewMessage(incoming=True))
@bot9.on(events.NewMessage(incoming=True))
@bot10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@bot.on(events.NewMessage(pattern="/replyraid"))
@bot2.on(events.NewMessage(pattern="/replyraid"))
@bot3.on(events.NewMessage(pattern="/replyraid"))
@bot4.on(events.NewMessage(pattern="/replyraid"))
@bot5.on(events.NewMessage(pattern="/replyraid"))
@bot6.on(events.NewMessage(pattern="/replyraid"))
@bot7.on(events.NewMessage(pattern="/replyraid"))
@bot8.on(events.NewMessage(pattern="/replyraid"))
@bot9.on(events.NewMessage(pattern="/replyraid"))
@bot10.on(events.NewMessage(pattern="/replyraid"))
async def _(e):
    global que
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        manisha = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(manisha[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
