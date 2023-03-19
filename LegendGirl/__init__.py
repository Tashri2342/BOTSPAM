import time

from .Config import *
from .core import *
from .Resources import *

start_time = time.time()
# Sudo Users

# full debugging
if SUDO_USERS:
    try:
        sudouser = str(SUDO_USERS).split(" ")
        print(sudouser)
        _list = []
        for x in sudouser:
            print(x)
            _list.append(int(x))
    except Exception as e:
        global SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User")
