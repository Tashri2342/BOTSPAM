#ChauhanMahesh/Vasusen/COL/DroneBots

import asyncio
from .. import bot, AUTH
from telethon import events

@bot.on(events.NewMessage(incoming=True))
async def u(event):
    au = AUTH.split(",")
    if event.is_private:
        if f'{event.sender_id}' not in au:
            await event.reply("You're not authorized to use me!")
            return
    if (str(event.text)).lower().startswith("spam:"): 
        if f'{event.sender_id}' not in au:
            await event.reply("You're not authorized to use me!")
            return
        reply = await event.get_reply_message()
        if not reply:
            await event.reply("Reply to any message.")
            return
        if not len((event.text).split(" ")) == 4:
            await event.reply("**ERROR:** Incorrect format\n\nFormat: `spam: sleep_time spam_range chat`")
            return
        sleep = 1
        total = 0
        chat = 123456789
        try:
            sleep = int((event.text).split(" ")[1])
            total = int((event.text).split(" ")[2])
            if int((event.text).split(" ")[3]) == 0:
                chat = event.chat_id
            else:
                chat = int((event.text).split(" ")[3]) 
        except ValueError:
            await event.reply("Sleep_time and spam_range should be integers.")
            return
        try:
            for i in range(total):
                try:
                    if sleep == 0:
                        await event.client.send_message(chat, reply) 
                    else:
                        await event.client.send_message(chat, reply) 
                        await asyncio.sleep(sleep)
                except FloodWaitError as fw:
                    await asyncio.sleep(fw.seconds + 5)
        except Exception as e:
            await event.client.send_message(event.chat_id, f"**SPAM FAILED**\n\nError: {str(e)}")
                
            
            
            
            
            
            
