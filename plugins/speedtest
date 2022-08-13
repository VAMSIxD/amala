import os
import wget
import speedtest

from PIL import Image
from pyrogram.types import Message
from pyrogram import filters, Client

from modules import app
from config import SUDO_USERS
from modules.database.onoff import is_on_off


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def run_speedtest(_, message):
    userid = message.from_user.id
    if await is_on_off(2):
        if userid in SUDOERS:
            pass
        else:
            return
    m = await message.reply_text("starting server test...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ running download speedtest")
        test.download()
        m = await m.edit("⚡️ running upload speedtest")
        test.upload()
        test.results.share()
    except speedtest.ShareResultsConnectFailure:
        pass
    except Exception as e:
        await m.edit_text(e)
        return
    result = test.results.dict()
    m = await m.edit_text("🔄 sharing speedtest results")
    if result["share"]:
        path = wget.download(result["share"])
        try:
            img = Image.open(path)
            c = img.crop((17, 11, 727, 389))
            c.save(path)
        except BaseException:
            pass
    output = f"""💡 **SpeedTest Results**
    
<u>**Client:**</u>

**ISP:** {result['client']['isp']}
**Country:** {result['client']['country']}
  
<u>**Server:**</u>

**Name:** {result['server']['name']}
**Country:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Latency:** {result['server']['latency']}  

⚡ **Ping:** {result['ping']}"""
    if result["share"]:
        msg = await app.send_photo(
            chat_id=message.chat.id, photo=path, caption=output
        )
        os.remove(path)
    else:
        msg = await app.send_message(
            chat_id=message.chat.id, text=output
        )
    await m.delete()
