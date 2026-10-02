![huricane](https://cdn.discordapp.com/attachments/773016620687294508/1555462022299131904/huricane.gif?backend=b2&ex=6ac09c65&is=6abf4ae5&hm=7c3efeecc541612a743cee6e0658f3233a0ca9378999e2f9cd715edae4163d93&)

<h2>How the final project should work</h2>

1. Feed the program my .ttml file I got from Cider
2. Parses the .ttml file in order to get the timings for what each frame should display
3. Makes all the frames and combines them into a video using ffmpeg
4. Also combines the .mp3 file into the ffmpeg video in order to make the final music video

<h2>To Do</h2>

1. ~~Need to optimise how im currently generating frames. Currently im just saving a bunch of photos so for longer inputs it requires a hefty amount of space and takes a long time~~
2. **Be able to parse .ttml files for lyrics rather than just taking input for video lyrics and final file name**
3. Rework how the imagecreation class currently works in order to support the more specific word timing the .ttml files have
4. Make it so the final video file actually combines with the original song's mp3 file
