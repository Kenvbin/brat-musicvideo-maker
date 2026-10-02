from PIL import Image, ImageDraw, ImageFilter, ImageFont


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
        newLine = 0

        for i in wordLength:
            if (i + total >= 15):
                newSentence = newSentence + "\n"
                total = i
                newLine+=1
                if (newLine == 3):
                    newSentence = ""
                    newLine = 0

            else:
                total = i + total + 1
            newSentence = newSentence + wordArray[iteration] + " "
            iteration = iteration + 1

        return newSentence
    
    def make_image(textforPrep, frameNum):

        W, H = 900,900
        font = ImageFont.truetype("font/ArialNarrowRegular.ttf", 90)

        textforImage = imagecreation.prep_sentence(textforPrep)
        
        imageName = "frames/frame" + str(frameNum) + ".png"
        frame = Image.new(mode="RGB", size=(W,H), color =(255,255,255))
        writeText = ImageDraw.Draw(frame)

        _, _, w, h = writeText.textbbox((0, 0), textforImage, font=font)
        writeText.text(((W-w)/2, (H-h)/2), textforImage, font = font, fill=0)

        finishedFrame = frame.filter(ImageFilter.GaussianBlur(2))

        finishedFrame.save(imageName, "PNG")
