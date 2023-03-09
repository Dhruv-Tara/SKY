# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807


from pyrogram import *
from pyrogram.types import *
from SKY import *

@app.on_callback_query()
async def inq(client:Client,query : CallbackQuery):
    ""
    qry = query.data.lower()
    if qry == "del_s":
        if query.from_user.id == query.message.reply_to_message.from_user.id:

            await app.answer_callback_query(
                query.id,
                "Deleted"
            )
            await client.delete_messages(
                query.message.chat.id,
                query.message.id
            )
            
        else :
            await app.answer_callback_query(
                query.id,
                "Not For You",
                show_alert= True
            )