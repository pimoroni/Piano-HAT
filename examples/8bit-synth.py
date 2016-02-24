#!/usr/bin/env python

import pianohat
import pygame
import numpy
import time
import math
import signal

print("""
8-bit Piano HAT

This advanced example demonstrates software synthesis.

It uses pygame's sndarray.make_sound method to create
8bit tones with specific frequency, bitrate and samplerates.

The octave up/down and instrument buttons are not supported (yet).

Please wait while Pygame is set up and samples are generates...

Press CTRL+C to exit!
""")

BITRATE = 8
SAMPLERATE = 11025

def play_sample(channel, pressed):
    if pressed:
        notes[channel].play(loops=-1)
    else:
        notes[channel].fadeout(1)

def generate_sample(frequency=440, duration=1, bit_rate=8, sample_rate=11025):
    sample_count = int(round(duration*sample_rate))

    buffer = numpy.zeros((sample_count, 2), dtype = numpy.int16)
    max_sample = 2**(bit_rate-1) - 1

    #r = sample_rate / float(frequency) # Sawtooth

    r = 2*math.pi*frequency # Sine

    for s in range(sample_count):
        t = float(s)/sample_rate # Time index

        m = math.sin(r*t) # Sine

        #m = (s % r) / r # Sawtooth
        
        buffer[s][0] = int(round(max_sample*m))
        buffer[s][1] = buffer[s][0]

    sound = pygame.sndarray.make_sound(buffer)

    return sound

print("Initializing subsystem...")
pygame.mixer.pre_init(SAMPLERATE, -BITRATE, 4, 512)
pygame.mixer.init()

print("Generating samples...")
notes = [generate_sample(frequency=f, duration=1) for f in [
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
    ]]

pianohat.on_note(play_sample)
print("Ready...")

signal.pause()
