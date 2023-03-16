# starting all clients
from LegendGirl.Config import *

if ":" in BOT_TOKEN:
    Client1 = Client(
        "LegendSpam",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="LegendGirl.LegendBoy"),
    )
    print("LegendSpam : Bot token 1 has been found")
else:
    print("LegendSpam : Client 1 not Found")


if BOT_TOKEN2:
    Client2 = Client(
        "LegendSpam2",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN2,
        plugins=dict(root="LegendGirls.LegendBoy"),
    )
    print("LegendSpam : Bot token 2 Found")
else:
    Client2 = None


if BOT_TOKEN3:
    Client3 = Client(
        "LegendSpam3",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN3,
        plugins=dict(root="LegendGirls.LegendBoy"),
    )
    print("LegendSpam : Bot token 3 Found")
else:
    Client3 = None


if BOT_TOKEN4:
    Client4 = Client(
        "LegendSpam4",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN4,
        plugins=dict(root="LegendGirls.LegendBoy"),
    )
    print("LegendSpam - [INFO]: Bot token 4 Found")
else:
    Client4 = None
