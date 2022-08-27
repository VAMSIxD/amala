## ©copyright infringement on Telugu Coders

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters          
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from modules.clientbot import clientbot
from config import GROUP, NETWORK, BOT_USERNAME

## don't change any value in this repo if you change the value bot will crash your heroku accounts. 


@Client.on_callback_query(filters.regex("home_start"))
async def home_start(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})\n
➠ ɴᴏ ʟᴀɢ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
➠ ɪᴡɪʟʟ ᴘʟᴀʏ sᴏɴɢs sᴍᴏᴏᴛʜʟʏ ᴀɴᴅ sᴏғᴛʟʏ. 
➠ ʀᴜɴɴɪɴɢ ᴏɴ ᴠᴘs sᴇʀᴠᴇʀ. 
➠ ᴘʀᴏᴠɪᴅᴇᴅ ᴠɪᴅᴇᴏ sᴜᴘᴘᴏʀᴛ. 
➠ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters) 

ᴛʜᴀɴᴋ ʏᴏᴜ ❤🌹ᴀɴʏ:\n\nɪssᴜᴇ ᴀʙᴏᴜᴛ ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀs.""", 
    reply_markup=InlineKeyboardMarkup(
        [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/Tc_shadowo")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url="https://t.me/telugucoders"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/tgshadow_fighters"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝗖𝗼𝗺𝗺𝗮𝗱𝘀❱", callback_data="command_list"),
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

   

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ ʜᴇʟʟᴏ ɴᴀᴍsᴛʜᴇ ᴀɴɴᴀ ᴛʜɪs ɪs ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ɢᴜɪᴅᴇ ᴡʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ɴᴇᴅᴅ sᴇʟᴇᴄᴛ ʜᴇʀᴇ.. 

➠ ᴛʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters) 
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("sᴋɪᴘ", callback_data="skip_list"), 
            InlineKeyboardButton("ᴘᴀᴜsᴇ", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("ʀᴇsᴜᴍᴇ", callback_data="resume_list"), 
            InlineKeyboardButton("sᴛᴏᴘ", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="play_list"), 
            InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="source"), 
            ],[
            InlineKeyboardButton("◁", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
async def general_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🍀 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ)  ɴᴏᴛ /ᴘʟᴀʏ - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ\n
➠ /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ\n
➠ /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ\n
➠ /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs\n
➠ /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs\n
➠ /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)\n
➠ /help - ᴛᴏ sʜᴏᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ (ғᴜʟʟ ʙᴏᴛ ɢᴜɪᴅᴇ)\n
➠ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
async def skip_list(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""👋🏻 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/skip ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ sᴋɪᴘ ᴛᴏ ɴᴇxᴛ sᴏɴɢ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/teamshadowprojects)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💘 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/pause ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ɪɴ ɢʀᴏᴜᴘ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""❤ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/resume ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/Team_shadowmusic_bot)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/end ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴇɴᴅ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/play ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴘʟᴀʏ ᴀ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..\n\n vplay (ᴠɪᴅᴇᴏ)**

➠ **ᴅᴇsɪɢɴᴇᴅ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("source"))
async def source(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""❣️ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

➠  **ᴛʜɪs ɪs ᴛʜᴇ ᴀᴍᴀʟᴀ ᴍᴜsɪᴄ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ ᴀ ⭐ sᴛᴀʀᴛ ᴛᴏ ʀᴇᴘᴏ""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("sᴏᴜʀᴄᴇ", url="https://github.com/TeluguCodersMusic/Amalav2.0")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ɪs ᴀ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ɪɴ sᴏ ᴍᴀɴʏ sᴇʀᴠᴇʀ's, ɪᴛ's ᴏɴʟɪɴᴇ sɪɴᴄᴇ 𝟷sᴛ ᴊᴜɴᴇ 𝟸𝟶𝟸𝟸 ᴀɴᴅ ɪᴛ's ᴄᴏɴsᴛᴀɴᴛʟʏ ᴜᴘᴅᴀᴛᴇᴅ \n
➠ ᴛʜɪs ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) \n 
➠ © ᴏɴ ʙᴇʜᴀʟғ ᴏғ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/tgshadow_fighters)
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 ʙɪɴ", callback_data="close_panel")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
