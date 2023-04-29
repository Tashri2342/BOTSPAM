import asyncio
import platform

from LegendBS.start_bot import start_bot
from pyrogram import __version__ as py_version
from pyrogram import idle

from .core.clients import *

loop = asyncio.get_event_loop()





if __name__ == "__main__":
    loop.run_until_complete(Start_BotSpam())
    print(" Good Bye ! ")
