from pyrogram.types import InlineKeyboardButton

Class Data:
    HELP_MENU = [
        [
            InlineKeyboardButton(
                text="✨ Support ✨", url=f"https://t.me/LegendBotSpam"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧸 Add me in your group", callback_data="help"
            ),
        ],
        [
            InlineKeyboardButton(
            text="❄️ Source Code ❄️", callback_data="lol"
            ),
        ],
    ]
    
