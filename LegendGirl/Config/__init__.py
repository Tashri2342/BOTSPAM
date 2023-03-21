import os

ENV = bool(os.environ.get("ENV", False))

async def config(ENV):
    if ENV:
        from sample_config import *  # noqa
    elif os.path.exists("config.py"):
        from config import *  # noqa
    return *

Config = config(ENV)
