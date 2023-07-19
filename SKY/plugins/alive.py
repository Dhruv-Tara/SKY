# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from pyrogram import *
import pyrogram
from pyrogram.types import *
import sys
from SKY import *

@app.on_message(filters.command("alive"))
async def alive(_,msg:Message) -> None:
    "Works when /alive is written"
    cur = datetime.datetime.utcnow()
    usr = msg.from_user
    X = await app.get_me()
    await msg.reply_text(
        f"Hello {usr.first_name}\nI am alive now\nUptime : {uptime(cur)}\nPython : {sys.version.split(' ')[0]}\nPyrogram : {pyrogram.__version__}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support",url="https://t.me/monarchs_alley"),
                    InlineKeyboardButton("Help",url=f"https://t.me/{X.username}?start=help")
                ]
            ]
        )
    )