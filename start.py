import os
import sys
import time 
os.system("clear")


vars = """
APP_ID=
API_HASH=0
SUDO_USERS=
ALIVE_PIC=
HELP_PIC=
PING_PIC=
LOGS_CHANNEL=
HANDLER=
BOT_TOKEN=
BOT_TOKEN2=
BOT_TOKEN3=
BOT_TOKEN4=
BOT_TOKEN5=
BOT_TOKEN6=
BOT_TOKEN7=
BOT_TOKEN8=
BOT_TOKEN9=
BOT_TOKEN10=
BOT_TOKEN11=
BOT_TOKEN12=
BOT_TOKEN13=
BOT_TOKEN14=
BOT_TOKEN10=
BOT_TOKEN11=
BOT_TOKEN12=
BOT_TOKEN13=
BOT_TOKEN14=
BOT_TOKEN15=
BOT_TOKEN16=
BOT_TOKEN17=
BOT_TOKEN18=
BOT_TOKEN19=
BOT_TOKEN20=
BOT_TOKEN21=
BOT_TOKEN22=
BOT_TOKEN23=
BOT_TOKEN24=
BOT_TOKEN25=
"""


def bot_start():
    os.system("clear")
    ask = input("Do You Want to Start Bot Spam y/n: ")
    if ask.lower() == "y":
        os.system("python3 -m LegendGirl")
    elif ask.lower() == "n":
        print("\nOk! You Can Start It Later With by using; python3-m LegendGirl\n")
        sys.exit()
    else:
        os.system("clear")
        print("\nInput Must Be y or n")
        bot_start()


def check_again():
    recheck = input(f"\nHave You Filled ALL Vars Correctly?: y/n: ")
    if recheck.lower() == "n":
        os.system("clear")
        print(f"Ohh! Now Fill Your Vars Again")
    elif recheck.lower() == "y":
        get_start()
    else:
        print(f"\n{ask}Input Must Be Y or N")
        check_again()


def LegendStartUP():
    app_id = input(f"pEnter APP_ID: ")
    if app_id:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set APP_ID {app_id}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    api_hash = input(f"\nEnter API_HASH: ")
    if api_hash:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set API_HASH {api_hash}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    HELP_PIC = input(f"\nEnter HELP_PIC (Telegraph link) or press enter!: ")
    if HELP_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set HELP_PIC {HELP_PIC}")
    PING_PIC = input(f"\nEnter PING_PIC (Telegraph link) or press enter!: ")
    if PING_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set PING_PIC {PING_PIC}")
     HELP_PIC = input(f"\nEnter HELP_PIC (Telegraph link) or press enter!: ")
    if START_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set START_PIC {START_PIC}")
    LOG_CHANNEL = input(f"\Enter Chat ID or Username of LOG_CHANNEL or press enter: ")
    if LOG_CHANNEL:
        print("Got it! Fill next value")
        os.system(f"dotenv set LOG_CHANNEL {LOG_CHANNEL}"
    sudo_users = input(f
L"\nEnter SUDO_USERS (space by space) or press enter: ").replace(" ", "\ ")
    if sudo_users:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set SUDO_USERS {sudo_users}")
    cmd_hndlr = input(f"\n{ask}Enter HANDLER or press enter: ")
    if cmd_hndlr:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set HANDLER {cmd_hndlr}")
    BOT_TOKEM = input(f"\nEnter session or bot token of CLIENT: ")
    if CLIENT:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT {CLIENT}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        SpamX_Setup()
    CLIENT2 = input(f"\n{ask}Enter session or bot token of CLIENT2 or press enter: ")
    if CLIENT2:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT2 {CLIENT2}")
    CLIENT3 = input(f"\n{ask}Enter session or bot token of CLIENT3 or press enter: ")
    if CLIENT3:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT3 {CLIENT3}")
    CLIENT4 = input(f"\n{ask}Enter session or bot token of CLIENT4 or press enter: ")
    if CLIENT4:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT4 {CLIENT4}")
    CLIENT5 = input(f"\n{ask}Enter session or bot token of CLIENT5 or press enter: ")
    if CLIENT5:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT5 {CLIENT5}")
    CLIENT6 = input(f"\n{ask}Enter session or bot token of CLIENT6 or press enter: ")
    if CLIENT6:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT6 {CLIENT6}")
    CLIENT7 = input(f"\n{ask}Enter session or bot token of CLIENT7 or press enter: ")
    if CLIENT7:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT7 {CLIENT7}")
    CLIENT8 = input(f"\n{ask}Enter session or bot token of CLIENT8 or press enter: ")
    if CLIENT8:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT8 {CLIENT8}")
    CLIENT9 = input(f"\n{ask}Enter session or bot token of CLIENT9 or press enter: ")
    if CLIENT9:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT9 {CLIENT9}")
    CLIENT10 = input(f"\n{ask}Enter session or bot token of CLIENT10 or press enter: ")
    if CLIENT10:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT10 {CLIENT10}")
    CLIENT11 = input(f"\n{ask}Enter session or bot token of CLIENT11 or press enter: ")
    if CLIENT11:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT11 {CLIENT11}")
    CLIENT12 = input(f"\n{ask}Enter session or bot token of CLIENT12 or press enter: ")
    if CLIENT12:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT12 {CLIENT12}")
    CLIENT13 = input(f"\n{ask}Enter session or bot token of CLIENT13 or press enter: ")
    if CLIENT13:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT13 {CLIENT13}")
    CLIENT14 = input(f"\n{ask}Enter session or bot token of CLIENT14 or press enter: ")
    if CLIENT14:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT14 {CLIENT14}")
    CLIENT15 = input(f"\n{ask}Enter session or bot token of CLIENT15 or press enter: ")
    if CLIENT15:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT15 {CLIENT15}")
    CLIENT16 = input(f"\n{ask}Enter session or bot token of CLIENT16 or press enter: ")
    if CLIENT16:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT16 {CLIENT16}")
    CLIENT17 = input(f"\n{ask}Enter session or bot token of CLIENT17 or press enter: ")
    if CLIENT17:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT17 {CLIENT17}")
    CLIENT18 = input(f"\n{ask}Enter session or bot token of CLIENT18 or press enter: ")
    if CLIENT18:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT18 {CLIENT18}")
    CLIENT19 = input(f"\n{ask}Enter session or bot token of CLIENT19 or press enter: ")
    if CLIENT19:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT19 {CLIENT19}")
    CLIENT20 = input(f"\n{ask}Enter session or bot token of CLIENT20 or press enter: ")
    if CLIENT20:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT20 {CLIENT20}")
    database_url = input(f"\n{ask}Enter Postgres database url or press enter: ")
    if database_url:
        if 'postgresql' in database_url or 'postgres' in database_url:
           print(f"{bcyan}Got it!")
           os.system(f"dotenv set DATABASE_URL {database_url}")
        else:
           print(f"{error}Need Postgres database url, fill DATABASE_URL manually")
    recheck()


botspam = input(f"{ask}Want to fill vars ? if yes type Y/yes else press enter: ")
if botspam.lower() in ["y", "yes"]:
    if not os.path.exists(".env"):
        y = open(".env", "w")
        y.write(vars)
        y.close()
        os.system("clear")
        LegendStartUP()
    if os.path.exists(".env"):
        f = open(".env")
        check = f.read()
        print(check)
        x.close()
        check_again()
        if not len(lines) == 35:
            os.system("rm -rf .env")
            y = open(".env", "w")
            y.write(vars)
            y.close()
            os.system("clear")
            LegendStartUP()
        else:
            os.system("clear")
            LegendStartUP()
else:
    os.system("clear")
    os.system("python3 -m LegendGirl")
