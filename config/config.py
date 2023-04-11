import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
que = {}
admins = {}

#------------------------ Important Stuff 😌 -----------------------

API_ID = int(getenv("API_ID", "26514346"))
API_HASH = getenv("API_HASH", "cc6e77c20c2ab98b1fc1ad53bee2a475")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQBcx78XWXnq3RJHGeUSUAfIwTRNjvfR11JdJ8E1Z6sWG67sVsMtisAYBN3ikPJzz9Dry_W6a2YIUFkEensd8a0oaP1laSEEw0fzawENGTIJtvRzwOA511pF5koE_y53mtsxRG4NoUvdsa6nV0LyUg_NYVU0qLpotqkMSEukcvby2t0W14qcDSu3PpEwwTQ8F8-8JuunfUPSFHOIZ362vhjZ2Q80z4XlRvezwSZcynEfmf4Y14ugO820oxbzSwOleY-0CbKr1tDBC8xNTDUvz8ebDu4DhJ0jauwOZDXNwuFdozYQmj701gi2l6EA4iTWxL8dCofH69imYyHKxK7gMNeaAAAAAWVbr2IA")
BOT_USERNAME = getenv("BOT_USERNAME", "@Musicuuuuuuuuuuubot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5556040702 5589457533 5566634044").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6232201171").split())
)  # Input type must be interger

#•••••••••••••••••••••••• Mongodb Url Stuff •••••••••••••••••••••••

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://galaxina:galaxina@galaxina.ejvfqm7.mongodb.net/?retryWrites=true&w=majority")

#________________________ Updates 🍃 & Music bot name_______________________________

NETWORK = getenv("NETWORK", "Missrose")
GROUP = getenv("GROUP", "Missrose")
BOT_NAME = getenv("BOT_NAME"_ "Crazy")

#************************* Image Stuff 💕 **************************

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png") 
aiohttpsession = aiohttp.ClientSession()


