# NOTE this one is specifically for playlist compilations
import random
import os
from tkinter import CENTER, Image
from moviepy.editor import *
import datetime

# TODO video type option generation (loop vs still image)
# TODO ambient sound options

#### AUDIO #####

playlist=[]
# get all music
for filename in os.listdir('./audio'):
    f = os.path.join('./audio', filename)
    if os.path.isfile(f) and filename.endswith('.mp3'):
        # append to music
        playlist.append(f)

# shuffle so it's not alphabetical
random.shuffle(playlist)

# add audio clips (music) together into one file
clips = [AudioFileClip(c) for c in playlist]
final_audio_clip = concatenate_audioclips(clips)
final_audio_clip.write_audiofile('./compiled/audio.mp3')

#### DESCRIPTION #####
# TODO keywords/tags

# get timestamps
unformatted_timestamps = [0]
for i in range(1, len(playlist)): # note that (start, stop), stop is ommited
    t = round(clips[i].duration) + unformatted_timestamps[i-1]
    if(t >= 3600): over_a_hour = True
    unformatted_timestamps.append(t)

timestamps=[]
# format timestamps properly - TODO: changes depeding on if it's over an hour or under
for t in unformatted_timestamps: timestamps.append(str(datetime.timedelta(seconds=t)))

# TODO description into to a file

## VIDEO ##

## TODO: generate image version (no need to use pillow)
## TODO: looped video version

#https://zulko.github.io/moviepy/_modules/moviepy/video/compositing/CompositeVideoClip.html#:~:text=%5Bdocs%5Dclass%20CompositeVideoClip(VideoClip,width)%20of%20the%20final%20clip.
## image version
image = (ImageClip("./upload-image-here/image.jpg")
          .set_duration(final_audio_clip.duration)
          .set_pos(CENTER)
          .set_fps(0.1))

video = concatenate_videoclips([image], method='chain')
video.audio = CompositeAudioClip([AudioFileClip("./compiled/audio.mp3")])
video.write_videofile('./compiled/video.mp4',fps=0.1)

## TODO UPLOAD ##
# title
# description
# timestamps
# video
# thumbnail

## CLEANING ##
# audio downloads
# for filename in os.listdir('./audio'):
#     f = os.path.join('./audio', filename)
#     if os.path.isfile(f) and filename.endswith('.mp3'):
#         # remove file
#         os.remove(f)
