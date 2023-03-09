# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807
# Credits to SOME1HING FOR AI QUOTES 

from SKY import *
from pyrogram import *
from pyrogram.types import *
import InspiroQuotes

Q = InspiroQuotes.Quote()

@app.on_message(filters.command("quote"))
async def quotes(_,msg:Message) -> None:
    "Returns a AI generated quote made my SOME1HING"
    photo = Q.quote()
    await msg.reply_photo(photo)