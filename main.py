import os

from makeimage import imagecreation
from makevideo import videoCreation

if not os.path.exists("videos"):
    os.mkdir("videos")
if not os.path.exists("frames"):
    os.mkdir("frames")
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
gradualText = ""
iteration = 0

for x in textToWrite:
    gradualText = gradualText + x
    imagecreation.make_image(gradualText, iteration)
    iteration = iteration + 1

videoCreation.export(title)
