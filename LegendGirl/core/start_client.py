version = "v1.0"
group_username = "@LegendBotSpam"

from LegendBS.start_bot import start_bot

from LegendGirl.Config import *

if BOT_TOKEN:
    BOT_TOKEN1 = BOT_TOKEN
else:
    pass

# def Start_BotSpam():
#     if BOT_TOKEN:
#         start_bot(Client1)

#     if BOT_TOKEN2:
#         try:
#             start_bot(Client2)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN3:
#         try:
#             start_bot(Client3)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN4:
#         try:
#             start_bot(Client4)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN5:
#         try:
#             start_bot(Client5)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN6:
#         try:
#             start_bot(Client6)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN7:
#         try:
#             start_bot(Client7)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN8:
#         try:
#             start_bot(Client8)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN9:
#         try:
#             start_bot(Client9)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN10:
#         try:
#             start_bot(Client10)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN11:
#         try:
#             start_bot(Client11)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN12:
#         try:
#             start_bot(Client12)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN13:
#         try:
#             start_bot(Client13)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN14:
#         try:
#             start_bot(Client14)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN15:
#         try:
#             start_bot(Client10)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN16:
#         try:
#             start_bot(Client16)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN17:
#         try:
#             start_bot(Client17)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN18:
#         try:
#             start_bot(Client18)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN19:
#         try:
#             start_bot(Client19)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN20:
#         try:
#             start_bot(Client20)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN21:
#         try:
#             start_bot(Client21)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN22:
#         try:
#             start_bot(Client22)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN23:
#         try:
#             start_bot(Client23)
#         except Exception as e:
#             print(e)

#     if BOT_TOKEN24:
#         try:
#             start_bot(Client24)
#         except Exception as e:
#             print(e)
#     if BOT_TOKEN25:
#         try:
#             start_bot(Client25)
#         except Exception as e:
#             print(e)

#     print("➖➖➖➖➖➖➖➖➖➖➖➖")
#     print(f"🔥 Bot Spam 🔥[INFO] : Group Username {group_username}")
#     print(f"🔥 Bot Spam 🔥[INFO] : Version - {platform.python_version()}")
#     print(f"🔥 Bot Spam 🔥[INFO]: SpamBot Version - {version}")
#     print(f"🔥 Bot Spam 🔥[INFO]: Pyrogram Version - {py_version}")
#     print("➖➖➖➖➖➖➖➖➖➖➖➖")
#     idle()

"""
def Start_BotSpam():
    threads = []
    for i in range(2, 26):
        try:
            var = globals()[f"BOT_TOKEN{i}"]
            if var is not None:
                t = threading.Thread(target=start_bot, args=(var,))
                threads.append(t)
                t.start()
        except AttributeError as e:
            print(e)

    for t in threads:
        t.join()
"""


def Start_BotSpam():
    for i in range(1, 26):
        var = globals()[f"BOT_TOKEN{i}"]
        if var is not None:
            start_bot(var)
