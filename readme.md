# Welcome to Youtube Automator Bot

## Create A Automated Compiled Playlist
#### NOTES
+ Only JPG is supported right now... (but you can manually change it in the code to support other types?)

#### HOW TO USE
1. Create your playlist on youtube, or yt music
2. edit `link` in download_music.py, or run the following command:
`youtube-dl -x --audio-format mp3 -o "./audio/%(title)s.%(ext)s" %YOUR LINK%`
3. run mainlpy and wait for it to compile the video
4. upload the video by using this command:
`python upload_video.py --file="./compiled/video.mp4" --title="%%YOUR TITLE%%" --description="%%YOUR DESCRIPTION%%" --keywords="%%KEYWORD, KEYWORD%%" --category="10" --privacyStatus="public"`