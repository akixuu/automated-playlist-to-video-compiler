# Create A Automated Compiled Playlist Video

#### NOTES
+ Only a JPG image is supported right now
+ use a youtube or yt music playlist

#### HOW TO USE
1. Create your playlist on youtube, or yt music
2. edit `link` in download_music.py, or run the following command:
`youtube-dl -x --audio-format mp3 -o "./audio/%(title)s.%(ext)s" %YOUR LINK%`
3. run mainlpy and wait for it to compile the video
4. upload the video by using this command:
`python upload_video.py --file="./compiled/video.mp4" --title="%YOUR_TITLE%" --description="%YOUR_DESCRIPTION%" --keywords="%KEYWORD,KEYWORD%" --category="10" --privacyStatus="public"`
Note that category 10 is a code to signify it's a music-related video

#### INCOMING UPDATES
+ fully automate all steps
+ create a backlog vids scheduled for upload
+ support different background types (looping vids, auto-generated formatted bgs, repeating slideshows)
+ add image filters (make bg slowly moving)
+ add audio filters (8bit, 8d, etc)
+ update text in the vid depending on the song that is playing
+ improve render times
+ support looping music
+ create nice descriptions and metadata (w/timestamps, keywords)
+ detect if copyrighted (ignore copyrighted music -> note that you can also manually do this step by selectively choosing music)