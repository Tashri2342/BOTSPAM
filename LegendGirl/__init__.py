import time

from .Config import *
from .core import *
from .Resources import *

start_time = time.time()
version = "v1.0"
group_username = "@LegendUserBot_XD"
# Sudo Users

sudouser = []
if SUDO_USERS:
    sudouser = str(SUDO_USERS).split(" ")
    _list = []
    for x in sudouser:
        _list.append(int(x))
else:
    print("Add Key Sudo User")
