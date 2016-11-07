#!/usr/bin/env python

import math
import signal
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

try:
    import pygame
except ImportError:
    exit("This script requires the pygame module\nInstall with: sudo pip install pygame")

import pianohat


print("""
8-bit Piano HAT

This advanced example demonstrates software synthesis.

It uses pygame's sndarray.make_sound method to create
8bit tones with specific frequency, bitrate and samplerates.

Instrument = Toggle Sine Wave
Octave ^ = Toggle Saw Wave
Octave V = Toggle Square Wave

Please wait while Pygame is set up and samples are generated...

Press CTRL+C to exit!
""")

BITRATE = 8
SAMPLERATE = 44100

ATTACK_MS=25
RELEASE_MS=500

# Fee; free to change the volume!
volume = {'sine':0.8, 'saw':0.4, 'square':0.4}

wavetypes = ['sine','saw','square']
enabled = {'sine':True, 'saw':False, 'square':False}
notes = {'sine':[],'saw':[],'square':[]}


# The samples are 8bit signed, from -127 to +127
# so the max amplitude of a sample is 127
max_sample = 2**(BITRATE - 1) - 1

def handle_instrument(channel, pressed):
    """Handles the Instrument, Octave Up/Down keys
    These toggle Sine, Saw and Square waves on and off so you can combine them
    """
    if not pressed:
        return

    if channel == 15: # Sine
        enabled['sine'] = not enabled['sine']
        print("Sine: {}".format("ON" if enabled['sine'] else "OFF"))
    if channel == 14: # Saw
        enabled['saw'] = not enabled['saw']
        print("Saw: {}".format("ON" if enabled['saw'] else "OFF"))
    if channel == 13: # Square
        enabled['square'] = not enabled['square']
        print("Square: {}".format("ON" if enabled['square'] else "OFF"))

    update_leds()


def play_sample(channel, pressed):
    """Handles the piano keys
    Any enabled samples are played, and *all* samples are turned off is a key is released
    """
    pianohat.set_led(channel, pressed)
    if pressed:
        for t in wavetypes:
            if enabled[t]:
                notes[t][channel].play(loops=-1, fade_ms=ATTACK_MS)
    else:
        for t in wavetypes:
            notes[t][channel].fadeout(RELEASE_MS)


def wave_sine(freq, time):
    """Generates a single sine wave sample"""
    s = math.sin(2*math.pi*freq*time)
    return int(round(max_sample * s ))


def wave_square(freq, time):
    """Generates a single square wave sample"""
    return -max_sample if freq*time < 0.5 else max_sample


def wave_saw(freq, time):
    """Generates a single sav wave sample"""
    s = ((freq*time)*2) - 1
    return int(round(max_sample * s)) 


def update_leds():
    """Updates the Instrument and Octave LEDs to show enabled samples"""
    pianohat.set_led(15, enabled['sine'])
    pianohat.set_led(14, enabled['saw'])
    pianohat.set_led(13, enabled['square'])


def generate_sample(frequency, volume=1.0, wavetype=None):
    """Generates a sample of a specific frequency and wavetype"""
    if wavetype is None:
        wavetype = wave_square

    sample_count = int(round(SAMPLERATE/frequency))

    buf = numpy.zeros((sample_count, 2), dtype = numpy.int8)

    for s in range(sample_count):
        t = float(s)/SAMPLERATE # Time index
        buf[s][0] = wavetype(frequency, t)
        buf[s][1] = buf[s][0] # Copy to stero channel

    sound = pygame.sndarray.make_sound(buf)
    sound.set_volume(volume) # Set the volume to balance sounds

    return sound


print("Initializing subsystem...")
pygame.mixer.pre_init(SAMPLERATE, -BITRATE, 4, 256)
pygame.mixer.init()
pygame.mixer.set_num_channels(32)


print("Generating samples...")
for f in [
        261.626,
        277.183,
        293.665,
        311.127,
        329.628,
        349.228,
        369.994,
        391.995,
        415.305,
        440.000,
        466.164,
        493.883,
        523.251
    ]:
    notes['sine'] += [generate_sample(f, volume=volume['sine'], wavetype=wave_sine)]
    notes['saw'] += [generate_sample(f, volume=volume['saw'], wavetype=wave_saw)]
    notes['square'] += [generate_sample(f, volume=volume['square'], wavetype=wave_square)]


pianohat.auto_leds(False)
pianohat.on_note(play_sample)
pianohat.on_instrument(handle_instrument)
pianohat.on_octave_up(handle_instrument)
pianohat.on_octave_down(handle_instrument)
update_leds()


print("Now, make beautiful music...")


signal.pause()
