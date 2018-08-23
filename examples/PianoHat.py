import pianohat
import time
from pygame import mixer
my_sound_files = [
    "/home/pi/Downloads/despacito.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/despacito.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/despacito.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav",
    "/home/pi/Downloads/Metal.wav"]
def handle_note(channel, pressed):
    if pressed:
        my_sounds[channel].play(loops=0)
        print("you pressed key {}".format(channel))
    else:
        print("you released key{}".format(channel))
mixer.init(22050, -16, 2, 512)
mixer.set_num_channels(13)
my_sounds = [mixer.Sound(sound_file) for sound_file in my_sound_files] 
pianohat.on_note(handle_note)

    
while True:
    time.sleep(.001)

         