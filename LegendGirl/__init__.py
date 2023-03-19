import time

from .core import *
from .Config import *
from .Resources import *

start_time  = time.time()

#Sudo Users

sudoser = []
if SUDO_USERS:
  sudoser = str(SUDO_USERS).split(" ")
  _list = []
  for x in sudouser:
        _list.append(int(x))
else:
  print("Add Key Sudo User")