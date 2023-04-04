from pyrogram.types import InlineKeyboardButton


class Data:
    HELP_MENU1 = [
        [
            InlineKeyboardButton(text="⚜️ banall ⚜️, callback_data="banall"),
            InlineKeyboardButton(text="📍birthday 📍", callback_data="birthday"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Ping ⚜️, callback_data="core_help1"),
            InlineKeyboardButton(text="📍 Restart 📍", callback_data="core_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ eval ⚜️, callback_data="evaluators_help1"),
            InlineKeyboardButton(text="📍 exec 📍", callback_data="evaluators_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Good Morning ⚜️, callback_data="gwish_help1"),
            InlineKeyboardButton(text="📍Good Afternoon 📍", callback_data="gwish_help2"),
            InlineKeyboardButton(text="⚜️ Good Night ⚜️, callback_data="gwish_help3"),           
        ],
        [
            InlineKeyboardButton(text="⚜️ Love Raid ⚜️, callback_data="lslove_help1"),
            InlineKeyboardButton(text="📍Love Reply Raid📍", callback_data="lslove_help2"),
            InlineKeyboardButton(text="⚜️ Love Dreply Raid ⚜️, callback_data="lslove_help3"),
            InlineKeyboardButton(text="📍 List Raid 📍", callback_data="lslove_help4"),          
        ],
        [
            InlineKeyboardButton(text="⚜️ Raid ⚜️, callback_data="raid_help1"),
            InlineKeyboardButton(text="📍Reply Raid📍", callback_data="raid_help2"),
            InlineKeyboardButton(text="⚜️ Dreply Raid ⚜️, callback_data="raid_help3"),
            InlineKeyboardButton(text="📍 List Raid 📍", callback_data="raid_help4"),          
        ]
        [
            InlineKeyboardButton(text="Close ", callback_data="close"),
        ],
    ]

    # For Future Purpose
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
