import importlib
import logging
import sys
from pathlib import Path


def load_plugins(plugin_name):
    path = Path(f"LegendGirl/LegendBoy/{plugin_name}.py")
    name = "LegendGirl.LegendBoy.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["LegendGirl.LegendBoy." + plugin_name] = load
    print("💝[Bot Spam]💝 ~ Has Imported " + plugin_name)


async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)
