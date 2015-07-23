#!/usr/bin/env python

import pianohat
import pygame
import time
import signal
import os
import re

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

melody = [
  0,0,7,7,9,9,7,
  5,5,4,4,2,2,0
]

note = 0
starting_note = 45

def next():
    global note
    pianohat.set_led(current_note(), False)
    time.sleep(0.1)
    note+=1
    note%=len(melody)
    pianohat.set_led(current_note(), True)

def current_note():
    return melody[note]

files = [
  './sounds/piano/39172__jobro__piano-ff-025.wav',
  './sounds/piano/39173__jobro__piano-ff-026.wav',
  './sounds/piano/39174__jobro__piano-ff-027.wav',
  './sounds/piano/39175__jobro__piano-ff-028.wav',
  './sounds/piano/39176__jobro__piano-ff-029.wav',
  './sounds/piano/39177__jobro__piano-ff-030.wav',
  './sounds/piano/39178__jobro__piano-ff-031.wav',
  './sounds/piano/39179__jobro__piano-ff-032.wav',
  './sounds/piano/39180__jobro__piano-ff-033.wav',
  './sounds/piano/39181__jobro__piano-ff-034.wav',
  './sounds/piano/39182__jobro__piano-ff-035.wav',
  './sounds/piano/39183__jobro__piano-ff-036.wav',
  './sounds/piano/39184__jobro__piano-ff-037.wav'
]

samples = [pygame.mixer.Sound(sample) for sample in files]

pianohat.auto_leds(False)

def handle_note(channel, pressed):
    if not channel == current_note():
        return

    if channel < len(samples) and pressed:
        print('Playing Sound: {}'.format(files[channel]))
        samples[channel].play(loops=0)
        next()

def handle_instrument(channel, pressed):
    pass

def handle_octave_up(channel, pressed):
    pass

def handle_octave_down(channel, pressed):
    pass

for x in range(16):
    pianohat.set_led(x, False)

pianohat.on_note(handle_note)
pianohat.on_octave_up(handle_octave_up)
pianohat.on_octave_down(handle_octave_down)
pianohat.on_instrument(handle_instrument)

pianohat.set_led(current_note(), True)

signal.pause()
