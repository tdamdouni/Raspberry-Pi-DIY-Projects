import explorerhat
import signal

def toggle_output(channel, event):
    print("Got {} on channel {}".format(event, channel))
    if channel < 5:
        explorerhat.light[channel-1].write(event=='press')
        explorerhat.output[channel-1].write(event=='press')
        
explorerhat.touch.pressed(toggle_output)
explorerhat.touch.released(toggle_output)

signal.pause()