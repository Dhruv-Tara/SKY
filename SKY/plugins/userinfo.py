# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807


from pyrogram.types import Message
from pyrogram import filters
from SKY import *
from pyrogram.enums.parse_mode import ParseMode
import os
from pyrogram.errors import PeerIdInvalid


Button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Delete",callback_data="del_s")
        ]
    ]
)

@app.on_message(filters.command("info"), group=3)
@app.on_edited_message(filters.command('info'))
async def info(_,msg:Message):
    m = await msg.reply_text("Searching...")
    if msg.reply_to_message:
        user = msg.reply_to_message.from_user.id

    elif not msg.reply_to_message and len(msg.command) == 1:
        user = msg.from_user.id
        
    elif not msg.reply_to_message and len(msg.command) != 1:
        user = msg.text.split(None, 1)[1]
        
    try: 
        x = await app.get_users(user)
        z = """User id : <code>{}</code> \nName : {} \nDC id : <code>{}</code>\nPermanent Link : <a href='tg://user?id={}'>{}</a>""".format(x.id,x.first_name,x.dc_id,x.id,x.first_name)

        if x.photo:
            if x.id in OWNERS:
                z += "\nThis Person is my Owner"
                file = x.photo.big_file_id  
                photo = await app.download_media(file)
                await msg.reply_photo(photo,
                    caption=z,parse_mode= ParseMode.HTML,
                    reply_markup=Button)
                os.remove(photo)
            else:
                file = x.photo.big_file_id  
                photo = await app.download_media(file)
                await msg.reply_photo(photo,
                    caption=z,parse_mode= ParseMode.HTML,
                    reply_markup=Button)
                os.remove(photo)
        else:
            await msg.reply_text(z,parse_mode=ParseMode.HTML,reply_markup=Button)
        await m.delete()
    except PeerIdInvalid:
        await m.edit_text("Try using `/info username of person`\nExample : `/info @Enmu_kizuki_bot`")

    
    
 