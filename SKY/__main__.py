#BSD 3-Clause License
#Copyright (c) 2023, Yash-Sharma-1807



from pyrogram import *
from SKY import *
from pyrogram.types import *
import asyncio
import datetime
from SKY.plugins import ALL_MODULES
import importlib
from .database.data import cur


loop = asyncio.get_event_loop()

async def main() -> None:
    "Normal code to start and idle the bot"

    global HELPABLE

    for module in ALL_MODULES:
        imported_module = importlib.import_module("SKY.plugins." + module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__

    bot_modules = ""
    tot = 0
    for i in ALL_MODULES:
        bot_modules += f"{i}\t"
        tot += 1
        
    LOGGER.info("LOADED THESE PLUGINS :")
    LOGGER.info(bot_modules)
    LOGGER.info(f"Total Number of plugins Loaded are {tot}")

    await app.start()
    await app.send_message(
        chat_id = Support,
        text=f"Started\nLoaded {tot} plugins"
    )
    LOGGER.info("Initializing connection with DB")
    cur.execute("Select 1")
    x = [y[0] for y in cur.fetchall()]
    if 1 in x :
        await app.send_message(
            chat_id = Support,
            text="Connected to DB"
        )
        LOGGER.info("Connected to DB")
    else : 
        await app.send_message(
            Support,
            "Can't connect to DB some Exception Occured"
        )
        LOGGER.info("Can't connect to DB some Exception Occured")

    await idle()
    await app.stop()

@app.on_message(filters.group & filters.command("start"))
async def start(_,msg:Message):
    cur = datetime.datetime.utcnow()
    await msg.reply_text(
        f"Hello\nAlive Since : {uptime(cur)}"
    )


@app.on_message(filters.private & filters.command("start"))
async def pmstart(client:Client,msg:Message):
    text = msg.text.split(" ")
    if len(text) > 1 and text[1] == "help":
        await msg.reply_text(
            "Soon"
        )
    elif len(text) > 1 and text[1] == "ok":
        await msg.reply_text(
            "OK"
        )
    else:
        cur = datetime.datetime.utcnow()
        usr = msg.from_user
        await msg.reply_text(
            f"Hello {usr.first_name}\nAlive Since : {uptime(cur)}"
        )
        await client.send_message(
            Support,
            f"{usr.mention} just started the bot"
        )

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt :
        LOGGER.info("Shutting Down SKY")