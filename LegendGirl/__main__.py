from pyrogram import Client

from LegendGirl.Config import *

tokens = []
for i in tokens:
    tokens.append(BOT_TOKEN2)

Client1 = Client(
    "LegendSpam",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="LegendGirl.LegendBoy"),
)

clients = [Client1]
i = 0
for token in tokens:
    if ":" in token:
        i = i + 1
        Client2 = Client(
            f"app{i}",
            bot_token=f"{token}",
            api_id=api_id,
            api_hash=api_hash,
            plugins=plugins,
        )
        clients.append(Client2)


async def main():
    await compose(clients)


Client1.run(main())
