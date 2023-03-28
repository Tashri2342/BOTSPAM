import platform

from pyrogram import __version__ as py_version
from pyrogram import idle

version = "v1.0"
group_username = "@LegendBotSpam"
from LegendBS.start_bot import start_bot

from LegendGirl.Config import *

from .clients import *


def Start_BotSpam():
    if BOT_TOKEN:
        start_bot(Client1)

    if BOT_TOKEN2:
        try:
            start_bot(Client2)
        except Exception as e:
            print(e)l0
  
    if BOT_TOKEN3:
        try:
            start_bot(Client3)
        except Exception as e:
            print(e)

    if BOT_TOKEN4:
        start_bot(Client4)

    if BOT_TOKEN5:
        start_bot(Client5)

    if BOT_TOKEN6:
        start_bot(Client6)

    if BOT_TOKEN7:
        start_bot(Client7)

    if BOT_TOKEN8:
        start_bot(Client8)

    if BOT_TOKEN9:
        start_bot(Client9)

    if BOT_TOKEN10:
        start_bot(Client10)

    if BOT_TOKEN11:
        start_bot(Client11)

    if BOT_TOKEN12:
        start_bot(Client12)

    if BOT_TOKEN13:
        start_bot(Client13)

    if BOT_TOKEN14:
        start_bot(Client14)

    if BOT_TOKEN15:
        start_bot(Client15)

    if BOT_TOKEN16:
        start_bot(Client16)

    if BOT_TOKEN17:
        start_bot(Client17)

    if BOT_TOKEN18:
        start_bot(Client18)

    if BOT_TOKEN19:
        start_bot(Client19)

    if BOT_TOKEN20:
        start_bot(Client20)

    if BOT_TOKEN21:
        start_bot(Client21)

    if BOT_TOKEN22:
        start_bot(Client22)

    if BOT_TOKEN23:
        start_bot(Client23)

    if BOT_TOKEN24:
        start_bot(Client24)

    if BOT_TOKEN25:
        start_bot(Client25)

    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"🔥 Bot Spam 🔥[INFO] : Group Username {group_username}")
    print(f"🔥 Bot Spam 🔥[INFO] : Version - {platform.python_version()}")
    print(f"🔥 Bot Spam 🔥[INFO]: SpamBot Version - {version}")
    print(f"🔥 Bot Spam 🔥[INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()
