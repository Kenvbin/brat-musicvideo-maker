import os
import shutil


class videoCreation:

    def export(videoTitle):
        videoCommand = "ffmpeg -f image2 -r 1/0.1 -i frames/frame%01d.png -vcodec mpeg4 -y videos/" + videoTitle + ".mp4"
        os.system(videoCommand)
        shutil.rmtree("frames")