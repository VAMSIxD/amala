import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
que = {}
admins = {}

#------------------------ Important Stuff 😌 -----------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
BOT_USERNAME = getenv("BOT_USERNAME")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5556040702 5589457533 5566634044").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5566634044").split())
)  # Input type must be interger

#•••••••••••••••••••••••• Mongodb Url Stuff •••••••••••••••••••••••

MONGODB_URL = getenv("MONGODB_URL")

#________________________ Updates 🍃 & Music bot name_______________________________

NETWORK = getenv("NETWORK")
GROUP = getenv("GROUP")
BOT_NAME = getenv("BOT_NAME")

#************************* Image Stuff 💕 **************************

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png") 
aiohttpsession = aiohttp.ClientSession()


