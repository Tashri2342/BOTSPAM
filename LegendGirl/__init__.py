import time

from .Config import *
from .core import *

start_time = time.time()
# Sudo Users


def make_list(sudos):
    str_list = sudos.split(" ")
    _list = []
    for x in str_list:
        _list.append(int(x))
    return _list


sudoser = []
sudos = sudoser
# full debugging
if SUDO_USERS:
    try:
        sudoser = make_list(SUDO_USERS)
        print(sudoser)
    except Exception as e:
        sudoser = SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User")
