import os
import sys
import time

os.system("clear")


vars = """
APP_ID=
API_HASH=
SUDO_USERS=
START_PIC=
START_MESSAGE=
HELP_PIC=
PING_PIC=
LOG_CHANNEL=
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
        LegendStartUP()
    elif recheck.lower() == "y":
        bot_start()
    else:
        print(f"\nInput Must Be Y or N")
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
    START_PIC = input(f"\nEnter START_PIC (Telegraph link) or press enter!: ")
    if START_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set START_PIC {START_PIC}")
    START_MESSAGE = input(f"\nEnter START_MESSAGE (Telegraph link) or press enter!: ")
    if START_MESSAGE:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set START_MESSAGE{START_MESSAGE}")
    LOG_CHANNEL = input(f"\Enter Chat ID or Username of LOG_CHANNEL or press enter: ")
    if LOG_CHANNEL:
        print("Got it! Fill next value")
        os.system(f"dotenv set LOG_CHANNEL {LOG_CHANNEL}")
    sudo_users = input(f"\nEnter SUDO_USERS (space by space) or press enter: ").replace(
        " ", "\ "
    )
    if sudo_users:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set SUDO_USERS {sudo_users}")
    cmd_hndlr = input(f"\nEnter HANDLER or press enter: ")
    if cmd_hndlr:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set HANDLER {cmd_hndlr}")
    BOT_TOKEN = input(f"\nEnter session or bot token of BOT TOKEN: ")
    if BOT_TOKEN:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set BOT TOKEN {BOT_TOKEN}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    for i in range(2, 26):
        token = input(f"\nEnter session or bot token of BOT_TOKEN{i} or press enter: ")
        if token:
            print(f"Got it! Fill next value")
            os.system(f"dotenv set BOT_TOKEN{i} {token}")


botspam = input(f"Want to fill vars ? if yes type Y/yes else press enter: ")
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
