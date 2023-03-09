# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

import datetime
from SKY import app, uptime
from pyrogram import filters
from pyrogram.types import Message

@app.on_message(filters.command("ping"))
@app.on_edited_message(filters.command("ping"))
async def ping(_,msg:Message):
    start_time = datetime.datetime.now()
    x = await msg.reply_text("Pong..")
    end_time = datetime.datetime.now()
    tgping = (end_time - start_time).microseconds / 1000
    upt = datetime.datetime.utcnow()
    await x.edit_text("Current Ping : `{}` ms\nCurrent Uptime : `{}`".format(tgping,uptime(upt)))