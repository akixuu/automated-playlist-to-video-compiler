import os

link='https://music.youtube.com/playlist?list=PLKkLmqe_JXuiNPoS53Fh1MzcfvCQrse7v&'

# download music/clips FIXME better implementation
os.system(f'youtube-dl -x --audio-format mp3 -o "./audio/%(title)s.%(ext)s" {link}')
