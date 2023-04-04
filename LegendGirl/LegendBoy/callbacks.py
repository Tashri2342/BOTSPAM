from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from Data import Data
from LegendGirl.cmd_help import *


@Client.on_callback_query()
async def _callbacks(Legend: Client, callback_query: CallbackQuery):
    user = await Legend.get_me()
    user.mention
    query = callback_query.data.lower()
    if query.startswith("helpmenu1"):
        if query == "helpmenu1":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await Legend.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="Help Menu One Powered By @TeamLegendXD",
                reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
            )
    elif query == "helpmenu2":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Legend.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Help Menu Two Powered By @TeamLegendXD",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU2),
        )
    elif query == "helpmenu3":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Legend.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Help Menu Two Powered By @TeamLegendXD",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU3),
        )
    elif query == "banall":
        await callback_query.answer("banall", show_alert=True)
    elif query == "birthday":
        await callback_query.answer(birthday_help, show_alert=True)
