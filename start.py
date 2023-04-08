import os
import sys

os.system("clear")


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


botspam = input(f"{ask}Want to fill vars ? if yes type Y/yes else press enter: ")
if botspam.lower() in ["y", "yes"]:
    if not os.path.exists(".env"):
        y = open(".env", "w")
        y.write(vars)
        y.close()
        os.system("clear")
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
        else:
            os.system("clear")
else:
    os.system("clear")
    os.system("python3 -m LegendGirl")
