import glob
from pathlib import Path
from LegendGirl.utils import load_plugins
import logging
from . import bot, bot2, bot3, bot5 , bot6, bot7, bot8, bot9, bot10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "LegendGirl/LegendBoy/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Sir Deployed Ho Gya")
print("Congratulations")

if __name__ == "__main__":
    bot.run_until_disconnected()
    
if __name__ == "__main__":
    bot2.run_until_disconnected()

if __name__ == "__main__":
    bot3.run_until_disconnected()
    
if __name__ == "__main__":
    bot4.run_until_disconnected()

if __name__ == "__main__":
    bot5.run_until_disconnected()
    
if __name__ == "__main__":
    bot6.run_until_disconnected()

if __name__ == "__main__":
    bot7.run_until_disconnected()
    
if __name__ == "__main__":
    bot8.run_until_disconnected()

if __name__ == "__main__":
    bot9.run_until_disconnected()
    
if __name__ == "__main__":
    bot10.run_until_disconnected()

