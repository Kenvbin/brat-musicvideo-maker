from PIL import Image, ImageDraw, ImageFont


class imagecreation:

    #13 characters before wrap
    def prep_sentence(stringOfText):
        wordArray = []
        wordLength = []
        for word in stringOfText.split():
            wordArray.append(word)
            wordLength.append(len(word))

        total = 0
        newSentence = ""
        iteration = 0

        for i in wordLength:
            if (i + total > 13):
                newSentence = newSentence + "\n" + wordArray[iteration] + " "
                total = i
            else:
                newSentence = newSentence + wordArray[iteration] + " "
                total = i + total
            iteration = iteration + 1

        return newSentence
    
    def make_image(textforPrep, frameNum):

        W, H = 500,500
        font = ImageFont.truetype("font/Ldfcomicsans-jj7l.ttf", 50)

        textforImage = imagecreation.prep_sentence(textforPrep)
        
        imageName = "frames/frame" + str(frameNum) + ".png"
        frame = Image.new(mode="RGB", size=(W,H), color =(255,255,255))
        writeText = ImageDraw.Draw(frame)

        _, _, w, h = writeText.textbbox((0, 0), textforImage, font=font)
        writeText.text(((W-w)/2, (H-h)/2), textforImage, font = font, fill=0)

        frame.save(imageName, "PNG")
