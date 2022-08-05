#Thank to @teamyukki

from pyrogram import filters
from pyrogram.types import Message
from modules.helpers.decorators import authorized_users_only
from config import PRIVATE_BOT_MODE
from modules import app
from modules.helpers.filters import get_command
from modules.misc import SUDOERS
from modules.database import (add_private_chat,
                                       get_private_served_chats,
                                       is_served_private_chat,
                                       remove_private_chat)


@app.on_message(filters.command("authorize") & SUDOERS)
@authorized_users_only
async def authorize(client: Client, message: Message):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text("Private Bot Mode is disabled.\n\nTo use your bot as private bot make sure to set **PRIVATE_BOT_MODE** = **True**")
    if len(message.command) != 2:
        return await message.reply_text("**Usage:**\n/authorize [CHAT_ID]")
    try:
        chat_id = int(message.text.strip().split()[1])
    except:
        return await message.reply_text("Failed to verify chat_id.\n\nMake sure its numeric and in correct format. Don't use chat username or links.")
    if not await is_served_private_chat(chat_id):
        await add_private_chat(chat_id)
        await message.reply_text("Added given chat to authorized list")
    else:
        await message.reply_text("Chat is already in the authorized list")


@app.on_message(filters.command("unauthorize") & SUDOERS)
@authorized_users_only
async def unauthorize(client: Client, message: Message):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text("Private Bot Mode is disabled.\n\nTo use your bot as private bot make sure to set **PRIVATE_BOT_MODE** = **True**")
    if len(message.command) != 2:
        return await message.reply_text("**Usage:**\n/unauthorize [CHAT_ID]")
    try:
        chat_id = int(message.text.strip().split()[1])
    except:
        return await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ ᴄʜᴀᴛ_ɪᴅ.\n\nᴍᴀᴋᴇ sᴜʀᴇ ɪᴛs ɴᴜᴍᴇʀɪᴄ ᴀɴᴅ ɪɴ ᴄᴏʀʀᴇᴄᴛ ғᴏʀᴍᴀᴛ. ᴅᴏɴ'ᴛ ᴜsᴇ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʟɪɴᴋs.")
    if not await is_served_private_chat(chat_id):
        return await message.reply_text("ɴᴏ sᴜᴄʜ ᴄʜᴀᴛ ᴇxɪsᴛs ɪɴ ᴛʜᴇ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪsᴛ")
    else:
        await remove_private_chat(chat_id)
        return await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ ɢɪᴠᴇɴ ᴄʜᴀᴛ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪsᴛ")


@app.on_message(filters.command("authorized") & SUDOERS)
@authorized_users_only
async def authorized(client: Client, message: Message):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text("ᴘʀɪᴠᴀᴛᴇ ʙᴏᴛ ᴍᴏᴅᴇ ɪs ᴅɪsᴀʙʟᴇᴅ.\n\nᴛᴏ ᴜsᴇ ʏᴏᴜʀ ʙᴏᴛ ᴀs ᴘʀɪᴠᴀᴛᴇ ʙᴏᴛ ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ sᴇᴛ **PRIVATE_BOT_MODE** = **True**")
    m = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ.... ғᴇᴛᴄʜɪɴɢ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀᴛs.")
    served_chats = []
    text = "ғᴇᴛᴄʜᴇᴅ ᴄʜᴀᴛs:"
    chats = await get_private_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    count = 0
    co = 0
    msg = "ᴜɴғᴇᴛᴄʜᴇᴅ ᴄʜᴀᴛs:"
    for served_chat in served_chats:
        try:
            title = (await app.get_chat(served_chat)).title
            count += 1
            text += f"{count}:- {title[:15]} [{served_chat}]\n"
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            co += 1
            msg += f"{co}:- {title} [{served_chat}]\n"
    if co == 0:
        if count == 0:
            return await m.edit("ɴᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀᴛs ғᴏᴜɴᴅ")
        else:
            return await m.edit(text)
    else:
        if count == 0:
            await m.edit(msg)
        else:
            text = f"{text} {msg}"
            return await m.edit(text)
