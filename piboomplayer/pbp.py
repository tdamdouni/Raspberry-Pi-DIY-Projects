import os
import sys
import vlc

if __name__ == '__main__':
    filepath = "iwyb.mp3"
    movie = os.path.expanduser(filepath)
    if 'http://' not in filepath:
        if not os.access(movie, os.R_OK):
            print ( 'Error: %s file is not readable' % movie )
            sys.exit(1)
        instance = vlc.Instance("--aout=alsa", "--alsa-audio-device=default")
        try:
            media = instance.media_new(movie)
        except NameError:
            print ('NameError: % (%s vs Libvlc %s)' % (sys.exc_info()[1],
                           vlc.__version__, vlc.libvlc_get_version()))
            sys.exit(1)
        player = instance.media_player_new()
        player.set_media(media)
        player.play()
#dont exit!

# p = vlc.MediaPlayer("rr.mp3")
# p.play()

while(1):
    continue

