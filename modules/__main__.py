import asyncio
from pytgcalls import idle
from modules.clientbot import call_py, bot, user
from pyrogram import idle
from modules.logging import LOGGER

loop = asyncio.get_event_loop()


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("telugucoders")
    await user.join_chat("tgshadow_fighters")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
    LOGGER("modules").info("Stopping Telugu coders Music Bot! GoodBye")
