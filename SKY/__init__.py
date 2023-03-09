#BSD 3-Clause License
#Copyright (c) 2023, Yash-Sharma-1807


from pyrogram import *
from pyrogram.types import *
from .config import Config
import datetime
import logging


FORMAT = "[SKY] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger('[SKY]')
LOGGER.info("SKY is starting | Licensed under BSD 3-Clause License")
LOGGER.info("Project maintained by: github.com/Yash-Sharma-1807")


Token = Config.Token
Support = Config.Grp
API = Config.api
Hash = Config.hash
OWNERS = Config.Owner

app = Client(
    "Enmu",
    api_id=API,
    api_hash=Hash,
    bot_token=Token
)

now = datetime.datetime.utcnow()

def uptime(self)-> str:
    "Returns uptime"
    delta = self - now
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    if days:
        fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
    else:
        fmt = '{h} hours, {m} minutes, and {s} seconds'

    return fmt.format(d=days, h=hours, m=minutes, s=seconds) 