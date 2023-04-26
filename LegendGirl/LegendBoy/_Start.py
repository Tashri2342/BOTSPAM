from LegendBS.start import start_cmd
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from LegendGirl.Config import *
from LegendGirl import version
import platform
from ..core.clients import *
from pyrogram import __version__ as py_version


if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = "https://graph.org/file/89ed7d3a2bd8aa2c61385.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Legend: Client, message: Message):
    if ".jpg" in START_PIC or ".png" in START_PIC:
        my_detail = Client.get_me()
        my_mention = my_detail.mention
        if START_MESSAGE:
            START_MESSAGE = START_MESSAGE
        else:
            START_MESSAGE = (
                f"Hey👋 {message.from_user.mention}❤️\n✥I am {my_mention}\n❖═══❃≛⃝❈•✵•≛⃝❈❃═══❖\n✥ Pyrogram Version = {py_version}\n✥ Python Version = {platform.python_version()}\n✥ BotSpam Version = {version}\n❖═══❃≛⃝❈•✵•≛⃝❈❃═══❖"
            )
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    elif ".mp4" in START_PIC.lower():
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_video(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    else:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(
                    message.chat.id,
                    START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
