from os import getenv

from decouple import config

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)

HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)

BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
try:
    SUDO_USERS = str(getenv("SUDO_USERS", "123 456")).split(" ")
except Exception:
    SUDO_USERS = str(getenv("SUDO_USERS", "123 456"))

ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/315ec5fe03f2a612139b3.jpg")

ALIVE_MESSAGE = getenv("ALIVE_MESSAGE", "This is a Powerful Bot Spam Made By Team Legend")

PING_PIC = getenv("PING_PIC", "https://te.legra.ph/file/315ec5fe03f2a612139b3.jpg")

START_PIC = getenv("START_PIC", "https://te.legra.ph/file/315ec5fe03f2a612139b3.jpg")

LOG_CHANNEL = getenv("LOG_CHANNEL", None)

HANDLER = getenv("HANDLER", "/")
