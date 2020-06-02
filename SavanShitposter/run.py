import discord
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


if __name__ == "__main__":
    memeImg = Image.open("memeTemplate.png")
    draw = ImageDraw.Draw(memeImg)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.text((100, 600),"Savan, it's {}. Time to post\nCringe on the news channel.",fill = 'black', font=font)
    font = ImageFont.truetype("arial.ttf", 60)
    draw.text((630, 600),"Yes honey",fill = 'black', font=font)
    usrImg = Image.open("userImg.png")
    usrImg.thumbnail((400,400), Image.ANTIALIAS)
    memeImg.paste(usrImg,(600,300))

    memeImg.save("memeImg.png")
    memeImg.close()


