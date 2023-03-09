# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from pyrogram import *
from pyrogram.types import *
from ..database.data import DB , cur
from SKY import app

@app.on_message(filters.command("execute"))
async def execute(_,msg:Message) -> None:
    text = msg.text.split("/execute")
    cur.execute(f"{text[-1]}")
    await msg.reply_text(cur.fetchall())
    DB.commit()
    