import os

import ffmpegio

from makeimage import imagecreation

if not os.path.exists("videos"):
    os.mkdir("videos")

if not os.path.exists("font"):
    os.mkdir("font")

flag = os.O_RDONLY

try:
    os.open("font/ArialNarrowRegular.ttf", flag)
except FileNotFoundError:
    print("Font is missing from the font foler")
    raise

textToWrite = input("Write: ")

title = input("Title of video: ")
title= "videos/" + title + ".mp4"

gradualText = ""

def image_processor():
    global gradualText
    for x in textToWrite:
        gradualText = gradualText + x
        yield imagecreation.make_image(gradualText)

#Code bellow from "Video to/from Pillow Images" on ffmpegio doccumentation
with ffmpegio.open(
        title, # output file name
        "wv", # open file in write-video mode
        10/1, # framerate in frames/second
        pix_fmt="yuv420p", # specify the pixel format (default is yuv444p)
    ) as f:
    for frame in image_processor(): # frame is PIL Image
        f.write(frame)


