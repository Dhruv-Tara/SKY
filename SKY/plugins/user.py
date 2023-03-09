# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from SKY import *
from ..database.users import add_new

#------ID and Chats--------#

@app.on_message(filters.command("id"),group=10)
async def ids(client : Client,msg : Message) -> None:
    "Gives the id of chat and user"
    text = ""
    text += f"Chat ID : `{msg.chat.id}`"
    text += f"\n[Your ID](tg://user?id={msg.from_user.id}) : `{msg.from_user.id}`"
    text += f"\n[Message ID]({msg.link}) : `{msg.id}`"

    if not msg.reply_to_message:
        await msg.reply_text(text)

    elif msg.reply_to_message :
        text += f"\n[{msg.reply_to_message.from_user.first_name} User ID](tg://user?id={msg.reply_to_message.from_user.id}) : `{msg.reply_to_message.from_user.id}`"
        text += f"\n[Replied Message ID]({msg.reply_to_message.link}) : `{msg.reply_to_message.id}`"
        await msg.reply_text(text)



@app.on_message()
async def add_new_member_in_db(_,msg:Message) -> None :
    "Adds a new person to db if he is not in it"
    try :
        add_new(msg.from_user.id)
    except Exception :
        pass