import os
YOUR_NAME = os.environ.get("YOUR_NAME, None")
from .. import *
from telethon import events
from time import time
from datetime import datetime

@bot.on(
    events.NewMessage(pattern="^/help", func=lambda e: e.sender_id in SMEX_USERS)
)
async def ping(e):
    if e.sender_id in SMEX_USERS:
        text = "Help Menu Opening"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"Help Menu \n/bigspam ~ ex-/bigspam 102 SpamBot\n/spam ~ ex/spam 10 hello\n/restart - To Restart Ur App\n/ping - to show ur ping\n/raid - ex -/raid 10 replyto anyone message\n/replyraid ~ /replyraid reply to anyone message\n/dreplyraid ~ /dreplyraid reply to same person message\n/update ~ /update")
