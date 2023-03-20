L0
import platform

from pyrogram import __version__ as py_version
from pyrogram import idle

version = "v1.0"
group_username = "@LegendBot_OP"
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
    if Client:
        start_bot(Client)

    if Client2:
        start_bot(Client2)

    if Client3:
        start_bot(Client3)

    if Client4:
        start_bot(Client4)

    if Client5:
        start_bot(Client5)

    if Client6:
        start_bot(Client6)

    if Client7:
        start_bot(Client7)

    if Client8:
        start_bot(Client8)

    if Client9:
        start_bot(Client9)

    if Client10:
        start_bot(Client10)

    if Client11:
        start_bot(Client11)

    if Client12:
        start_bot(Client12)

    if Client13:
        start_bot(Client13)

    if Client14:
        start_bot(Client14)

    if Client15:
        start_bot(Client15)

    if Client16:
        start_bot(Client16)

    if Client17:
        start_bot(Client17)

    if Client18:
        start_bot(Client18)

    if Client19:
        start_bot(Client19)

    if Client20:
        start_bot(Client20)

    if Client21:
        start_bot(Client21)

    if Client22:
        start_bot(Client22)

    if Client23:
        start_bot(Client23)

    if Client24:
        start_bot(Client24)

    if Client25:
        start_bot(Client25)


    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"Legend Spam Bot [INFO] : Group Username {group_username}")
    print(f"Legend Spam Bot [INFO] : Version - {platform.python_version()}")
    print(f"Legend Spam Bot [INFO]: SpamBot Version - {version}")
    print(f"Legend Spam Bot  [INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()
