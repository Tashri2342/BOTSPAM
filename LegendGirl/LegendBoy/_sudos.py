from LegendBS.error import user_errors
from LegendBS.get_user import get_user
from pyrogram import Client, filters
from pyrogram.types import Message
import heroku3
from LegendGirl.Config import *

from .. import sudos

Heroku = heroku3.from_key(Config.API_KEY)
app = Heroku.app(HEROKU_APP_NAME)
heroku_var = app.config()

@Client.on_message(filters.user(sudos) & filters.command(["addsudo"], prefixes=HANDLER))
async def addsudo(Legend: Client, message: Message):
    if not HEROKU_APP_NAME:
        return await message.reply("Fill The Variable Of HEROKU_APP_NAME")
    try:
        user = await get_user(Legend, message)
    except Exception as e:
        await message.reply(user_errors(e))
        return
    if int(user.id) in sudos:
        await message.reply_text(f"User {user.mention} already in sudo list!")
        return
    heroku_var[SUDO_USERS] = user.id
    """sudos.append(int(user.id))
    print(sudos)"""
    await message.reply_text(f"User {user.mention} successfully promoted as Sudo!")


@Client.on_message(filters.user(sudos) & filters.command(["rmsudo"], prefixes=HANDLER))
async def remsudo(Legend: Client, message: Message):
    try:
        user = await get_user(Legend, message)
    except Exception as e:
        await message.reply(user_errors(e))
        return
    if int(user.id) not in sudos:
        await message.reply_text(f"User {user.mention} not in sudo list!")
        return
    sudos.remove(int(user.id))
    await message.reply_text(f"User {user.mention} successfully removed from Sudo!")


@Client.on_message(
    filters.user(sudos) & filters.command(["sudos", "sudolist"], prefixes=HANDLER)
)
async def sudolist(Legend: Client, message: Message):
    sudo_reply = "**Sudo users list - Legend Bot Spam** \n\n"
    for x in sudos:
        try:
            user = await Legend.get_users(x)
            sudo_reply += f" × {user.mention} \n"
        except:
            sudo_reply += f" × [{x}](tg://user?id={x}) \n"
    await message.reply_text(sudo_reply)
