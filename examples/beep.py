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
    "/home/pi/moo.wav",
    "/home/pi/dog.wav",
    "/home/pi/dog.wav",
    "/home/pi/moo.wav",
    "/home/pi/dog.wav",
    "/home/pi/moo.wav",
    "/home/pi/dog.wav",
    "/home/pi/moo.wav",
    "/home/pi/dog.wav",
    "/home/pi/moo.wav",
    "/home/pi/dog.wav",
    "/home/pi/moo.wav",
    "/home/pi/dog.wav"
]
my_sounds = [mixer.Sound(sound_file) for sound_file in my_sound_files]
pianohat.on_note(handle_note)
while True:
    time.sleep(0.001)
