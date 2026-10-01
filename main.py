from makeimage import imagecreation
from makevideo import videoCreation

textToWrite = input("Write: ")
gradualText = ""
iteration = 0


for x in textToWrite:
    gradualText = gradualText + x
    imagecreation.make_image(gradualText, iteration)
    iteration = iteration + 1

videoCreation.export("TestVideo")
