#Telugu coders 

import os
import requests
from modules import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiohttp import ClientSession
import re
import aiofiles
import aiohttp

session = ClientSession()
pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")
BASE = "https://batbin.me/"

async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]

@app.on_message(filters.command("paste") & ~filters.edited)
async def paste_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ `/paste`")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await message.reply_text("Only text and documents are supported")
    m = await message.reply_text("ᴘᴀsᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("You can only paste files smaller than 40KB.")
        if not pattern.search(r.document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    kb = [[InlineKeyboardButton(text="ᴘᴀsᴛᴇ ʟɪɴᴋ 💕", url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(photo=link,quote=False,caption="ᴘᴀsᴛᴇᴅ",reply_markup=InlineKeyboardMarkup(kb),)
        else:
            await message.reply_photo(photo=link,quote=False,caption="ᴘᴀsᴛᴇᴅ",reply_markup=InlineKeyboardMarkup(kb),)
        await m.delete()
    except Exception:
        await m.edit("ʜᴇʀᴇ's ʏᴏᴜʀ ᴘᴀsᴛᴇ", reply_markup=InlineKeyboardMarkup(kb))
