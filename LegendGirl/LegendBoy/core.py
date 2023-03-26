import datetime
import os
import sys
import time

from LegendBS.get_time import get_time
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl import start_time
from LegendGirl.Config import *

from .. import sudos


@Client.on_message(filters.user(sudos) & filters.command(["ping"], prefixes=HANDLER))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = get_time((time.time() - start_time))
    pong_msg = await e.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await pong_msg.edit_text(
        f"🔰Ping Pong🔰\n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}`"
    )


@Client.on_message(
    filters.user(sudos) & filters.command(["restart", "reboot"], prefixes=HANDLER)
)
async def restarter(Legend: Client, message: Message):
    await message.reply_text("**Re-starting...** \n Please wait!")
    try:
        await Legend.stop()
    except Exception as error:
        print(str(error))

    args = [sys.executable, "-m", "LegendGirl"]
    os.execl(sys.executable, *args)
    quit()
