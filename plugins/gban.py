#Telugu coders

""" global banned and un-global banned module """

import asyncio

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from modules.clientbot.clientbot import me_bot
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import bot_creator
from modules.database.dbchat import get_served_chats
from modules.database.dbpunish import add_gban_user, is_gbanned_user, remove_gban_user

from config import OWNER_ID, SUDO_USERS, BOT_USERNAME as bn


@Client.on_message(command(["gban", f"gban@{bn}"]) & other_filters)
@bot_creator
async def global_banned(c: Client, message: Message):
    BOT_NAME = me_bot.first_name
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**usage:**\n\n/gban [username | user_id]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = me_bot.id
        if user.id == from_user.id:
            await message.reply_text("You can't gban yourself !")
        elif user.id == BOT_ID:
            await message.reply_text("I can't gban myself !")
        elif user.id in SUDO_USERS:
            await message.reply_text("You can't gban sudo user !")
        elif user.id in OWNER_ID:
            await message.reply_text("You can't gban my creator !")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"🚷 **ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴɪɴɢ {user.mention}**\n⏱ ᴇxᴘᴇᴄᴛᴇᴅ ᴛɪᴍᴇ: `{len(served_chats)}`"
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
➥ **ɴᴇᴡ ɢʟᴏʙᴀʟ ʙᴀɴ ᴏɴ [{BOT_NAME}](https://t.me/{bn})

➥ **ᴏʀɪɢɪɴ:** {message.chat.title} [`{message.chat.id}`]
➥ **sᴜᴅᴏ ᴜsᴇʀ:** {from_user.mention}
➥ **ʙᴀɴɴᴇᴅ ᴜsᴇʀ:** {user.mention}
➥ **ʙᴀɴɴᴇᴅ ᴜsᴇʀ ɪᴅ:** `{user.id}`
➥ **ᴄʜᴀᴛs:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = me_bot.id
    if user_id == from_user_id:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ʏᴏᴜʀsᴇʟғ !")
    elif user_id == BOT_ID:
        await message.reply_text("ɪ ᴄᴀɴ'ᴛ ɢʙᴀɴ ᴍʏsᴇʟғ !")
    elif user_id in SUDO_USERS:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ sᴜᴅᴏ ᴜsᴇʀ !")
    elif user_id in OWNER_ID:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ᴍʏ ᴄʀᴇᴀᴛᴏʀ !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ɢʙᴀɴɴᴇᴅ !")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"🚷 **ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴɪɴɢ {mention}**\n⏱ ᴇxᴘᴇᴄᴛᴇᴅ ᴛɪᴍᴇ: `{len(served_chats)}`"
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
➥ **ɴᴇᴡ ɢʟᴏʙᴀʟ ʙᴀɴ ᴏɴ [{BOT_NAME}](https://t.me/{bn})

➥ **ᴏʀɪɢɪɴ:** {message.chat.title} [`{message.chat.id}`]
➥ **sᴜᴅᴏ ᴜsᴇʀ:** {from_user_mention}
➥ **ʙᴀɴɴᴇᴅ ᴜsᴇʀ:** {mention}
➥ **ʙᴀɴɴᴇᴅ ᴜsᴇʀ ɪᴅ:** `{user_id}`
➥ **ᴄʜᴀᴛs:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@Client.on_message(command(["ungban", f"ungban@{bn}"]) & other_filters)
@bot_creator
async def ungban_global(c: Client, message: Message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**usage:**\n\n/ungban [username | user_id]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = me_bot.id
        if user.id == from_user.id:
            await message.reply_text("You can't ungban yourself because you can't be gbanned !")
        elif user.id == BOT_ID:
            await message.reply_text("I can't ungban myself because i can't be gbanned !")
        elif user.id in SUDO_USERS:
            await message.reply_text("Sudo users can't be gbanned/ungbanned !")
        elif user.id in OWNER_ID:
            await message.reply_text("Bot creator can't be gbanned/ungbanned !")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("This user is not gbanned !")
            else:
                msg = await message.reply_text("» ᴜɴɢʙᴀɴɴɪɴɢ ᴜsᴇʀ...")
                await remove_gban_user(user.id)
                served_chats = []
                chats = await get_served_chats()
                for chat in chats:
                    served_chats.append(int(chat["chat_id"]))
                number_of_chats = 0
                for num in served_chats:
                    try:
                        await c.unban_chat_member(num, user.id)
                        number_of_chats += 1
                        await asyncio.sleep(1)
                    except FloodWait as e:
                        await asyncio.sleep(int(e.x))
                    except BaseException:
                        pass
                await msg.edit_text("✅ ᴛʜɪs ᴜsᴇʀ ʜᴀs ᴜɴɢʙᴀɴɴᴇᴅ")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = me_bot.id
    if user_id == from_user_id:
        await message.reply_text("You can't ungban yourself because you can't be gbanned !")
    elif user_id == BOT_ID:
        await message.reply_text("I can't ungban myself because i can't be gbanned !")
    elif user_id in SUDO_USERS:
        await message.reply_text("Sudo users can't be gbanned/ungbanned !")
    elif user_id in OWNER_ID:
        await message.reply_text("Bot creator can't be gbanned/ungbanned !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("This user is not gbanned !")
        else:
            msg = await message.reply_text("» ᴜɴɢʙᴀɴɴɪɴɢ ᴜsᴇʀ...")
            await remove_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.unban_chat_member(num, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except BaseException:
                    pass
                await msg.edit_text("✅ ᴛʜɪs ᴜsᴇʀ ʜᴀs ᴜɴɢʙᴀɴɴᴇᴅ")
