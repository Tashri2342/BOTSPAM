from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos


async def get_user(Legend, message):
    try:
        args = message.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        args = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
    elif args:
        user_ = args[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            await message.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
            return
        try:
            user = await Legend.get_users(user_)
        except (TypeError, ValueError):
            await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
            return
    else:
        await message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
        return

    return user


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
