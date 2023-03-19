import time

from .Config import *
from .core import *
from .Resources import *

start_time = time.time()
# Sudo Users
sudouser = []
# full debugging
if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(sudouser)
        _list = []
        for x in sudouser:
            _list.append(int(x))
    except Exception as e:
        sudouser = SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User")
