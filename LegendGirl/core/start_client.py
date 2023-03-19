import platform

from pyrogram import __version__ as py_version
from pyrogram import idle

from LegendGirl import group_username, version
from LegendGirl.Config import *

from .clients import *


def start_bot(Client):
    Client.start()
    try:
        x = Client.get_me()
        print(f"Client - [INFO]: @{x.username} get started ")
    except Exception as e:
        print(f"Error - {e}")


def Start_BotSpam():
    if CLIENT:
        start_bot(Client)

    if CLIENT2:
        start_bot(Client2)

    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"Legend Spam Bot [INFO] : Group Username {group_username}")
    print(f"Legend Spam Bot [INFO] : Version - {platform.python_version()}")
    print(f"Legend Spam Bot [INFO]: SpamBot Version - {version}")
    print(f"Legend Spam Bot  [INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()
