import os
from .. import *
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@bot.on(
    events.NewMessage(pattern="^/help", func=lambda e: e.sender_id in SMEX_USERS)
)
async def ping(e):
    if e.sender_id in SMEX_USERS:
        text = "Help Menu Opening"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"🤖Help Menu🤖 \n\n\n☞ /bigspam = To Bigspam Greater Then 100 \n➥ Usage - /bigspam 102 SpamBot \n\n☞ /spam = To Spam Less Than 100\n➥ usage - /spam 10 hello\n\n☞ /restart - To Restart Ur App\n\n☞ /ping - to show ur ping\n\n☞ /raid = To Raid The Person\n➥ Usage -/raid 10 reply to anyone message\n\n☞ /replyraid = To Raid The Automatically message after One Message By Enemy\n➥ Usage - /replyraid reply to anyone message\n\n☞ /dreplyraid ~ /dreplyraid reply to same person message\n\n☞ /update = To Update Your Userbot If You connected to repo with Heroku\n➥ Usage - /update")
