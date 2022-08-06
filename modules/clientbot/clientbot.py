import os
from pyrogram import idle
from pyrogram import Client as Bot
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from pytgcalls import PyTgCalls
from telethon import TelegramClient
   
bot = Bot(
    ":telugucoders:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

user = Client(
    STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

call_py = PyTgCalls(user, overload_quiet_mode=True) 
with Client(":telugucoders:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
