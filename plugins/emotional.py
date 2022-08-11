#Telugu Coders

import asyncio
import traceback

from pyrogram.types import Message
from pyrogram import Client, filters, __version__ as pyrover
from pytgcalls import (__version__ as pytgver)

from modules import __version__ as ver
from plugins.alive import __python_version__ as pyver

from modules.clientbot.clientbot import me_bot
from modules import app
from modules.helpers.filters import command
from modules.helpers.decorators import bot_creator, sudo_users_only
from modules.database.dbchat import get_served_chats, add_served_chat
from modules.database.dbusers import get_served_users
from modules.database.dbpunish import get_gbans_count
from modules.database.dbqueue import get_active_chats
from modules.database.dblockchat import blacklisted_chats
from config import BOT_USERNAME as uname
from config import SUDO_USERS

chat_watcher_group = 10

@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    chat_id = message.chat.id
    blacklisted_chats_list = await blacklisted_chats()

    if not chat_id:
        return

    if chat_id in blacklisted_chats_list:
        try:
            await USER.leave_chat(chat_id)
        except:
            pass
        return await app.leave_chat(chat_id)

    await add_served_chat(chat_id)

@app.on_message(command("gcast") & filters.user(SUDO_USERS))
async def broadcast_message(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**Broadcasted Message In {sent}  Chats with {pin} Pins.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text("**Usage**:\n/gcast [message]")
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✈️ **Broadcasted message in {sent} chats and {pin} pins.**"
    )

# Broadcast without pinned

@app.on_message(command("broadcast") & filters.user(SUDO_USERS) & ~filters.edited)
async def broadcast_message(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage**:\n/broadcast [message]")
    sleep_time = 0.1
    text = message.text.split(None, 1)[1]
    sent = 0
    schats = await get_served_chats()
    chats = [int(chat["chat_id"]) for chat in schats]
    m = await message.reply_text(
        f"Broadcast in progress, will take {len(chats) * sleep_time} seconds."
    )
    for i in chats:
        try:
            await app.send_message(i, text=text)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"✈️ **Broadcasted message in {sent} chats.**")


@Client.on_message(command(["stats", f"stats@{uname}"]) & ~filters.edited)
@sudo_users_only
async def bot_statistic(c: Client, message: Message):
    name = me_bot.first_name
    chat_id = message.chat.id
    msg = await c.send_message(
        chat_id, "❖ ᴄᴏʟʟᴇᴄᴛɪɴɢ sᴛᴀᴛs..."
    )
    served_chats = len(await get_served_chats()) 
    gbans_usertl = await get_gbans_count()
    tgm = f"""
📊 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛɪsᴛɪᴄ ᴏғ [{name}](https://t.me/{uname})`:`
➥ **ɢʀᴏᴜᴘs ᴄʜᴀᴛ** : `{served_chats}`
➥ **ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs** : `{gbans_usertl}`
➥ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{pyver}`
➥ **ᴘʏᴛɢᴄᴀʟʟs ᴠᴇʀsɪᴏɴ** : `{pytgver.__version__}`
➥ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{pyrover}`
➥ **ʙᴏᴛ ᴠᴇʀsɪᴏɴ** : `{ver}`"""
    await msg.edit(tgm, disable_web_page_preview=True)
