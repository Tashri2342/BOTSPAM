from LegendBS.get_user import get_user
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos


@Client.on_message(filters.me & filters.command(["addsudo"], prefixes=HANDLER))
async def addsudo(Legend: Client, message: Message):
    try:
        user = await get_user(Legend, message)
    except Exception as e:
        await message.reply(user_errors(e))
        return
    if int(user.id) in sudos:
        await message.reply_text(f"User {user.mention} already in sudo list!")
        return
    sudos.append(user.id)
    await message.reply_text(f"User {user.mention} successfully promoted as Sudo!")


@Client.on_message(filters.me & filters.command(["rmsudo"], prefixes=HANDLER))
async def remsudo(Legend: Client, message: Message):
    try:
        user = await get_user(Legend, message)
    except Exception as e:
        await message.reply(user_errors(e))
        return
    if int(user.id) not in sudos:
        await message.reply_text(f"User {user.mention} not in sudo list!")
        return
    sudos.remove(user.id)
    await message.reply_text(f"User {user.mention} successfully removed from Sudo!")


@Client.on_message(
    filters.me & filters.command(["sudos", "sudolist"], prefixes=HANDLER)
)
async def sudolist(Legend: Client, message: Message):
    sudo_reply = "**Sudo users list - SpamX** \n\n"
    for x in sudos:
        try:
            user = await Legend.get_users(x)
            sudo_reply += f" × {user.mention} \n"
        except:
            sudo_reply += f" × [{x}](tg://user?id={x}) \n"
    await message.reply_text(sudo_reply)
