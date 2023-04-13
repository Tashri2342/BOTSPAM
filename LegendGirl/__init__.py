import glob
import os
import time

from .Config import *
from .core import *

version = "v1"
group_username = "@LegendBotSpam"
start_time = time.time()


async def all_plugins():
    # This generates a list of plugins in this folder for the * in __main__ to
    # work.
    from glob import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob(dirname(__file__) + "/*.py")
    all_plugs = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return sorted(all_plugs)


# Sudo Users
sudos = []
# full debugging
if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(sudouser)
        _list = []
        for x in sudouser:
            _list.append(int(x))
        sudos = _list
    except Exception as e:
        sudos = SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User")
