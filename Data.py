from pyrogram.types import InlineKeyboardButton


class Data:
    HELP_MENU1 = [
        [
            InlineKeyboardButton(text="🔙 Previous", callback_data="helpmenu3"),
        ],
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="Next ⏭️", callback_data="helpmenu2"),
        ],
    ]

    HELP_MENU2 = [
        [
            InlineKeyboardButton(text="🔙 Previous", callback_data="helpmenu1"),
        ],
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="Next ⏭️", callback_data="helpmenu3"),
        ],
    ]
    HELP_MENU3 = [
        [
            InlineKeyboardButton(text="🔙 Previous", callback_data="helpmenu2"),
        ],
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="Next ⏭️", callback_data="helpmenu1"),
        ],
    ]
