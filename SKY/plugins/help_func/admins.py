# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from pyrogram import *
from pyrogram.types import *


async def can_ban(client : Client,msg : Message) -> bool :
    "returns weather a person can ban"
    can = await client.get_chat_member(msg.chat.id,msg.from_user.id)
    try :
        if can.privileges.can_restrict_members == True:
            return True
    except AttributeError :
        return False


async def can_unban(client: Client, msg : Message) -> bool :
    "returns weather a person can unban or not"
    can = await client.get_chat_member(msg.chat.id,msg.from_user.id)
    try :
        if can.privileges.can_restrict_members == True:
            return True
    except AttributeError :
        return False


async def is_admin(client : Client,msg, user_id) -> bool :
    "returns weather the replied user is a admin in that chat"
    can = await client.get_chat_member(msg.chat.id,user_id = user_id)
    try :
        if can.privileges :
            return True
    except AttributeError :
        return False


async def can_change_info(client : Client, msg : Message,user_id) -> bool:
    "returns boolean value weather a person can change group info and other stuff"
    can = await client.get_chat_member(msg.chat.id,user_id)
    try :
        if can.privileges.can_change_info == True:
            return True
    except AttributeError:
        return False