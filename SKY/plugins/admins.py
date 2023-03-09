# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807

from pyrogram import *
from pyrogram.types import *
from SKY import *
from .help_func.admins import can_ban,can_unban,is_admin,can_change_info
from datetime import datetime
import os

bot_cant = "Promote me to an admin with all rights."
admin_cant = "You lack admin rights to perform this action."

#---------------BAN---------------#

@app.on_message(filters.command("ban") & filters.group, group=1)
async def ban(client:Client,msg:Message) -> None:
    "bans a user only works in groups tho"
    X = await can_ban(client=client, msg= msg)
    if msg.reply_to_message:
        victim = msg.reply_to_message.from_user
        if X == True:
            admin = await is_admin(client,msg,victim.id)
            if admin == True:
                await msg.reply_text("I can't take this action against an Admin")
            elif admin == False:    
                await client.ban_chat_member(msg.chat.id,victim.id)
                await msg.reply_text(
                    f"Sucessfully banned {victim.first_name}",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                            InlineKeyboardButton("Unban",callback_data="unban")
                            ]
                        ]
                    )
                )
        elif X == False:
            await msg.reply_text("You lack permission")

    elif not msg.reply_to_message:
        if X == True:
            await msg.reply_text("Reply to a user to execute this command")
        elif X == False:
            await msg.reply_text("Reply to user and get admin rights to ban first.")

#------------UNBAN-------------------#

@app.on_message(filters.group & filters.command("unban"), group=2)
async def unban(client:Client,msg:Message)-> None:
    "unbans a user only works in groups tho"
    X = await can_unban(client=client, msg= msg)
    text = msg.text.split("/unban")
    
    if msg.reply_to_message:
        victim = msg.reply_to_message.from_user
        if X == True:
            await client.unban_chat_member(msg.chat.id,victim.id)
            await msg.reply_text(
                f"Sucessfully unbanned {victim.first_name}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("delete",callback_data="del_s")
                        ]
                    ]
                )
            )
        elif X == False:
            await msg.reply_text("You lack permission")
    elif not msg.reply_to_message:
        if X == True:
            await msg.reply_text("Reply to a user to execute this command")
        elif X == False:
            await msg.reply_text("Reply to user and get admin rights to ban first.")

#---------------SET GPIC------------#

@app.on_message(filters.command("setgpic") & filters.group , group=3)
async def setpfp(client : Client,msg:Message):
    "sets a pic as group pic"

    now = datetime.utcnow().second
    user_id = msg.from_user.id
    can = await can_change_info(client,msg,user_id)
    bot_can = await can_change_info(client,msg,client.me.id)
    directory_p = f"./downloads/{now}.jpg"
    directory_v = f"./downloads/{now}.mp4"

    if can == True :
        if bot_can == True :
            if msg.reply_to_message.photo :
                PHOTO = await client.download_media(msg.reply_to_message,directory_p)
            elif msg.reply_to_message.video:
                VIDEO = await client.download_media(msg.reply_to_message,directory_v)
            else :
                await msg.reply_text("Reply to a photo or video to set it as group profile picture.")
                pass
            try :
                if PHOTO:
                    await client.set_chat_photo(msg.chat.id,photo=PHOTO)
                    os.remove(directory_p)
                    await msg.reply_text("Sucessfully set new picture as group profile picture.")
                elif VIDEO :
                    await client.set_chat_photo(msg.chat.id,photo=VIDEO)
                    os.remove(directory_v)
                    await msg.reply_text("Sucessfully set new video profile picture of this chat.")
                else :
                    pass
            except Exception :
                await msg.reply_text("Some Exception occured try again.")
        else :
            await msg.reply_text(bot_cant)
    else :
        await msg.reply_text(admin_cant)



#-----------------GETADMINS------------#

@app.on_message(filters.group & filters.command("getadmins"))
async def getadmins(_,msg:Message):
    m = await msg.reply_text("Getting Admins And Bots....")
    AD = "ADMINS :-"
    BT = "\n\nBOTS :-"
    async for x in app.get_chat_members(msg.chat.id,filter= enums.ChatMembersFilter.ADMINISTRATORS):
        try:
            AD += "\n[{}](tg://user?id={})".format(x.user.first_name,x.user.id)
        except Exception as e:
            await m.edit_text(e)
    async for y in app.get_chat_members(msg.chat.id,filter=enums.ChatMembersFilter.BOTS):
        try:
            BT += "\n[{}](tg://user?id={})".format(y.user.first_name,y.user.id)
        except Exception as e:
            await m.edit_text(e)
    await m.delete()
    ALL = AD + BT
    await msg.reply_text(ALL)
