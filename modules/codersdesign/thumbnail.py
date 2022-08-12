# telugucoders
# thanks to @teamyukki

import os
import aiofiles
import aiohttp
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import ImageGrab
from modules.clientbot.clientbot import me_bot
from typing import Callable
from os import path
from config import BOT_NAME


def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""    
    for i in list:
        if len(text1) + len(i) < 27:        
            text1 += " " + i
        elif len(text2) + len(i) < 25:        
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()     
    return [text1,text2]

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image = Image.open(f"./background.png")
    black = Image.open("resource/black.jpg")
    img = Image.open("resource/robot.png")
    image5 = changeImageSize(1280, 720, img)
    image1 = changeImageSize(1280, 720, image)
    image1 = image1.filter(ImageFilter.BoxBlur(10))
    image11 = changeImageSize(1280, 720, image)
    image1 = image11.filter(ImageFilter.BoxBlur(10))
    image2 = Image.blend(image1,black,0.6)
    name_font = ImageFont.truetype("resource/font.ttf", 30)

    # Cropping circle from thumbnail
    image3 = image11.crop((280,0,1000,720))
    #lum_img = Image.new('L', [720,720] , 0)
   # draw = ImageDraw.Draw(lum_img)
   # draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
   # img_arr =np.array(image3)
    #lum_img_arr =np.array(lum_img)
    #final_img_arr = np.dstack((img_arr,lum_img_arr))
    #image3 = Image.fromarray(final_img_arr)
    image3 = image3.resize((500,500))
    

    image2.paste(image3, (100,115))
    image2.paste(image5, mask = image5)

    # fonts
    font1 = ImageFont.truetype(r'resource/robot.otf', 30)
    font2 = ImageFont.truetype(r'resource/robot.otf', 60)
    font3 = ImageFont.truetype(r'resource/robot.otf', 49)
    font4 = ImageFont.truetype(r'resource/Mukta-ExtraBold.ttf', 35)
    font5 = ImageFont.truetype(r'resource/font2.ttf', 70)

    image4 = ImageDraw.Draw(image2)

    # title
    title1 = truncate(title)
    image4.text((660, 280), text=title1[0], fill="white", font = font3, align ="left") 
    image4.text((660, 332), text=title1[1], fill="white", font = font3, align ="left") 

    # bot_name
    botname = f"{BOT_NAME}"

    image4.text((5, 5), text=botname, fill="white", font=name_font, width=32)

    # description
    nowplayingon = "NOW PLAYING"
    views = f"Views : {views}"
    duration = f"Duration : {duration} Minutes."
    channel = f"Requested By : {requested_by}"
     
    image4.text((690, 180), text=nowplayingon, fill="white", font = font5, stroke_width=2, stroke_fill="white") 
    image4.text((660, 410), text=views, fill="white", font = font4, align ="left", stroke_width=1, stroke_fill="red") 
    image4.text((660, 460), text=duration, fill="white", font = font4, align ="left", stroke_width=1, stroke_fill="pink") 
    image4.text((660, 510), text=channel, fill="white", font = font4, align ="left", stroke_width=1, stroke_fill="blue")

    
    image2.save(f"final.png")
    os.remove(f"background.png")
    final = f"temp.png"
    return final
