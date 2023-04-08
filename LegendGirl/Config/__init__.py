import os

from dotenv import load_dotenv

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import *  # noqa
elif os.path.exists("config.py"):
    from config import *  # noqa
elif os.path.exists(".env"):
    load_dotenv(".env")
