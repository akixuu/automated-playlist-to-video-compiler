# Create A Automated Compiled Playlist Video

#### NOTES
+ Only a JPG image is supported right now
+ use a youtube or yt music playlist

#### HOW TO USE
1. Create your playlist on youtube, or yt music
2. Run the following command:
`youtube-dl -x --audio-format mp3 -o "./audio/%(title)s - %(uploader)s.%(ext)s" <PLAYLIST_LINK_HERE>`
This command will download all the music from the playlist into `./audio` with the naming convention or `<title> - <author>.mp3`. Make sure the playlist you're choosing from is not private (so public or unlisted).
3. Upload a image (currently .jpg only) into the `./upload_image-here` dir. This will be the background for the duration of the video.
4. Run `python compile_video.py` and wait for the video to compile. The compiled video will be located in `./compiled/video.mp4`.
5. Upload the video to YouTube by using this command:
`python upload_video.py --file="./compiled/video.mp4" --title="<YOUR_TITLE>" --description="<YOUR_DESCRIPTION>%" --keywords="<KEYWORD,KEYWORD>" --category="10" --privacyStatus="public"`

#### INCOMING UPDATES
+ fully automate all steps (w/scheduler)
+ create a backlog vids scheduled for upload
+ support different background types (looping vids, auto-generated formatted bgs, repeating slideshows)
+ add image filters (make bg slowly moving, audio visualizer)
+ add audio filters (add ambient sounds, convert 8bit, 8d, etc)
+ update text in the vid depending on the song that is playing
+ update a slider in the vid depending on the time
+ improve render times
+ support looping music
+ create nice descriptions and metadata (w/timestamps, keywords)
+ detect if copyrighted (ignore copyrighted music -> note that you can also manually do this step by selectively choosing music)