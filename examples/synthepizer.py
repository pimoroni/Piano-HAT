import pianohat
import time
from pygame import mixer
def handle_note(channel, pressed):
    if pressed:
        my_sounds[channel].play(loops=0)
        print("You pressed key {}".format(channel))
    else:
        print("You released key {}".format(channel))
mixer.init(22050, -16, 2, 512)
mixer.set_num_channels(13)
my_sound_files = [
    "/home/pi/c.wav",
    "/home/pi/c#.wav",
    "/home/pi/d.wav",
    "/home/pi/eb.wav",
    "/home/pi/e.wav",
    "/home/pi/f.wav",
    "/home/pi/f#.wav",
    "/home/pi/g.wav",
    "/home/pi/g#.wav",
    "/home/pi/a.wav",
    "/home/pi/bb.wav",
    "/home/pi/b.wav",
    "/home/pi/synth.wav"

    
]
my_sounds = [mixer.Sound(sound_file) for sound_file in my_sound_files]
pianohat.on_note(handle_note)
while True:
    time.sleep(.001)
