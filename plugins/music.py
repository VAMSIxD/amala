# ©Telugu Coders music projects

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from modules.codersdesign.thumbnail import generate_cover
from modules.helpers.filters import command, other_filters
from modules.clientbot.queues import QUEUE, add_to_queue
from modules.clientbot import call_py, user
from modules.clientbot.utils import bash
from modules.helpers.gets import get_url, get_file_name
from config import BOT_USERNAME, IMG_5, DURATION_LIMIT, GROUP, NETWORK
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch

def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link: str):
    stdout, stderr = await bash(
        f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {link}'
    )
    if stdout:
        return 1, stdout
    return 0, stderr

#plus
useer = "NaN"

@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def play(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text(
            "you're an __Anonymous__ user !\n\n» revert back to your real user account to use this bot."
        )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 To use me, I need to be an **Administrator** with the following **permissions**:\n\n» ❌ __Delete messages__\n» ❌ __Invite users__\n» ❌ __Manage video chat__\n\nOnce done, type /reload"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "💡 To use me, Give me the following permission below:"
            + "\n\n» ❌ __Manage video chat__\n\nOnce done, try again."
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "💡 To use me, Give me the following permission below:"
            + "\n\n» ❌ __Delete messages__\n\nOnce done, try again."
        )
        return
    if not a.can_invite_users:
        await m.reply_text(
            "💡 To use me, Give me the following permission below:"
            + "\n\n» ❌ __Add users__\n\nOnce done, try again."
        )
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await c.unban_chat_member(chat_id, ubot)
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
    except UserNotParticipant:
        try:
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await m.reply_text(
                f"🍃 **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`"
            )
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...**")
            dl = await replied.download()
            link = replied.link
            
            try:
                if replied.audio:
                    songname = replied.audio.title[:70]
                    songname = replied.audio.file_name[:70]
                    duration = replied.audio.duration
                elif replied.voice:
                    songname = "Voice Note"
                    duration = replied.voice.duration
            except BaseException:
                songname = "Audio"
    
    await m.delete()
    audio = (
        (m.reply_to_message.audio or m.reply_to_message.voice)
        if m.reply_to_message
        else None
    )
    url = get_url(m) 

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"💡 Videos longer than {DURATION_LIMIT} minutes aren't allowed to play!"
            )
   
            if chat_id in QUEUE:
                title = songname
                userid = m.from_user.id
                requested_by = m.from_user.first_name
                duration = round(audio.duration / 60)
                views = "Locally added"
                thumbnail = f"{IMG_5}"
                image = await generate_cover(requested_by, title, views, duration, thumbnail)
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            "🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                await suhu.delete()
                await m.reply_photo(
                    photo="final.png",
                    reply_markup=buttons,
                    caption=f"**🍀ɴᴇxᴛ sᴏɴɢ ᴀᴛ ᴘᴏsɪᴛɪᴏɴ ɪɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs sᴇʀᴠᴇʀ... `{pos}` 🌷 ...**",
                )
            else:
                try:
                    title = songname
                    userid = m.from_user.id
                    requested_by = m.from_user.first_name
                    duration = round(audio.duration / 60)
                    views = "Locally added"
                    thumbnail = f"{IMG_5}"
                    image = await generate_cover(requested_by, title, views, duration, thumbnail)
                    await suhu.edit("🌹**ʏᴏᴜʀ sᴏɴɢ ɪs ᴘʀᴏᴄᴇssɪɴɢ ᴏɴ ᴍʏ sᴇʀᴠᴇʀ**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                            HighQualityAudio(),
                        ),
                        stream_type=StreamType().local_stream,
                    )
                    add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                    await suhu.delete()
                    buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            "🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                    await m.reply_photo(
                        photo="final.png",
                        reply_markup=buttons,
                        caption=f"**🍃ᴀᴍᴀʟᴀ ʀᴏʙᴏᴛ ᴀᴜᴅɪᴏ ᴘʟᴀʏɪɴɢ ᴏɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ᴘʀɪᴠᴀᴛᴇ sᴇʀᴠᴇʀ ....**",
                    )
                except Exception as e:
                    await suhu.delete()
                    await m.reply_text(f"🚫 ᴇʀʀᴏʀ:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "**✨ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ʙᴀʙʏ👶...**"
                )
            else:
                suhu = await c.send_message(chat_id, "🔍")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("**sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ʙᴀʙʏ...**")
                else:
                    results = YoutubeSearch(url, max_results=1).to_dict()
                    # print results
                    songname = search[0]
                    title = results[0]["title"]
                    url = results[0]["url"]
                    requested_by = m.from_user.first_name
                    duration = results[0]["duration"]
                    views = results[0]["views"]
                    thumbnail = results[0]["thumbnails"][0]
                    userid = m.from_user.id
                    image = await generate_cover(requested_by, title, views, duration, thumbnail)
                    coders, ytlink = await ytdl(url)
                    if coders == 0:
                        await suhu.edit(f"❌ ʏᴛ-ᴅʟ ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            "🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                            await m.reply_photo(
                                photo="final.png",
                                reply_markup=buttons,
                                caption=f"**🍀ɴᴇxᴛ sᴏɴɢ ᴀᴛ ᴘᴏsɪᴛɪᴏɴ ɪɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs sᴇʀᴠᴇʀ... `{pos}` 🌷...**",
                            )
                        else:
                            try:
                                await suhu.edit("🌹 **ʏᴏᴜʀ sᴏɴɢ ɪs ᴘʀᴏᴄᴇssɪɴɢ ᴏɴ ᴍʏ sᴇʀᴠᴇʀ**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("ᴍᴇɴᴜ", callback_data="menu"), 
                ],[
                        InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/{NETWORK}"),
                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"),  
                ],[
                        InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                                await m.reply_photo(
                                    photo="final.png",
                                    reply_markup=buttons,
                                    caption=f"**🍃ᴀᴍᴀʟᴀ ʀᴏʙᴏᴛ ᴀᴜᴅɪᴏ ᴘʟᴀʏɪɴɢ ᴏɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ᴘʀɪᴠᴀᴛᴇ sᴇʀᴠᴇʀ ...**",
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"🚫 ᴇʀʀᴏʀ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "**✨ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ʙᴀʙʏ👶..**"
            )
        else:
            suhu = await c.send_message(chat_id, "🔍")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("**sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ʙᴀʙʏ**")
            else:
                results = YoutubeSearch(query, max_results=5).to_dict()
                songname = search[0]
                title = results[0]["title"]
                url = search[1]
                requested_by = m.from_user.first_name
                duration = results[0]["duration"]
                views = results[0]["views"]
                thumbnail = results[0]["thumbnails"][0]
                userid = m.from_user.id
                image = await generate_cover(requested_by, title, views, duration, thumbnail)
                coders, ytlink = await ytdl(url)
                if coders == 0:
                    await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("ᴍᴇɴᴜ", callback_data="menu"), 
                ],[
                        InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/{NETWORK}"),
                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"),  
                ],[
                        InlineKeyboardButton("🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                        await m.reply_photo(
                            photo="final.png",
                            reply_markup=buttons,
                            caption=f"**🍀ɴᴇxᴛ sᴏɴɢ ᴀᴛ ᴘᴏsɪᴛɪᴏɴ ɪɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs sᴇʀᴠᴇʀ... `{pos}` 🌷 ...**",
                        )
                    else:
                        try:
                            await suhu.edit("🌹 **ʏᴏᴜʀ sᴏɴɢ ɪs ᴘʀᴏᴄᴇssɪɴɢ ᴏɴ ᴍʏ sᴇʀᴠᴇʀ**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            buttons = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("ᴍᴇɴᴜ", callback_data="menu"), 
                ],[
                        InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/{NETWORK}"),
                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"),  
                ],[
                        InlineKeyboardButton(
                            "🗑 ʙɪɴ", callback_data="set_close"), 
                ]
            ]
        )
                            await m.reply_photo(
                                photo="final.png",
                                reply_markup=buttons,
                                caption=f"**🍃ᴀᴍᴀʟᴀ ʀᴏʙᴏᴛ ᴀᴜᴅɪᴏ ᴘʟᴀʏɪɴɢ ᴏɴ ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs ᴘʀɪᴠᴀᴛᴇ sᴇʀᴠᴇʀ ...**",
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"🚫 ᴇʀʀᴏʀ: `{ep}`")

                        try:
                            os.remove("final.png")
                        except Exception:
                            pass
                        return

