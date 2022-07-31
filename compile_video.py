# NOTE this one is specifically for playlist compilations
import random, os, datetime
from tkinter import CENTER
from moviepy.editor import *

#### vars ####
render_fps = 0.1
image_filename = 'image.jpg'

# TODO rendering options
# image
# dynamic image
# looping video
# looping slideshow

# graphic/sfx options
# audio visualizer
# slow movement
# particles
# ambient noise loop

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

# get timestamps + clip lengths
audio_clip_lengths = [] # TODO use this later for dynamically changing image title and slider 
unformatted_timestamps = [0]
for i in range(1, len(playlist)): # note that (start, stop), stop is ommited
    t = round(int(clips[i-1].duration) + unformatted_timestamps[i-1])
    
    audio_clip_lengths.append(clips[i].duration)
    unformatted_timestamps.append(t)

timestamps=[]
# format timestamps properly - TODO: changes depeding on if it's over an hour or under
for t in unformatted_timestamps: timestamps.append(str(datetime.timedelta(seconds=t)))

# format under hour video timestamps
under_hour = False
if(final_audio_clip.duration < 3600): under_hour = True
if(under_hour):
    for i in range(len(timestamps)): timestamps[i] = timestamps[i][2:]

# create description FIXME: description ending and opening not working
with open("./compiled/description.txt", "w") as description:

        description_opening =''
        description_ending = ''

        with open('./edit_data_here/description_opening.txt') as f:
            description_opening = f.read()

        with open('./edit_data_here/description_ending.txt') as f:
            description_opening = f.read()

        description.write(description_opening + '\n\n')
        description.write('TIMESTAMPS\n')
        for i in range(len(timestamps)):
            description.write(timestamps[i] + ' || ' + playlist[i][8:-4] + '\n')

        description.write('\n\n' + description_ending)

## VIDEO ##

# still image bg
image = (ImageClip("./edit_data_here/" + image_filename)
          .set_duration(final_audio_clip.duration)
          .set_pos(CENTER)
          .set_fps(0.1))

video = concatenate_videoclips([image], method='chain')
video.audio = CompositeAudioClip([AudioFileClip("./compiled/audio.mp3")])
video.write_videofile('./compiled/video.mp4',fps=render_fps)
