#!/usr/bin/env python

import pianohat
import pygame
import signal
import glob
import os
import re
BANK = os.path.join(os.path.dirname(__file__), "sounds")

print("""
This example gives you a simple, ready-to-play instrument which uses .wav files.

For it to work, you must place directories of wav files in:

{}

We've supplied a piano and drums for you to get started with!

Press CTRL+C to exit.
""".format(BANK))

FILETYPES = ['*.wav', '*.ogg']
samples = []
files = []
octave = 0
octaves = 0

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(32)

patches = glob.glob(os.path.join(BANK, '*'))
patch_index = 0

if len(patches) == 0:
    exit("Couldn't find any .wav files in: {}".format(BANK))


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]


def load_samples(patch):
    global samples, files, octaves, octave
    files = []
    print('Loading Samples from: {}'.format(patch))
    for filetype in FILETYPES:
        files.extend(glob.glob(os.path.join(patch, filetype)))
    files.sort(key=natural_sort_key)
    octaves = len(files) / 12
    samples = [pygame.mixer.Sound(sample) for sample in files]
    octave = int(octaves / 2)


pianohat.auto_leds(True)


def handle_note(channel, pressed):
    channel = channel + (12 * octave)
    if channel < len(samples) and pressed:
        print('Playing Sound: {}'.format(files[channel]))
        samples[channel].play(loops=0)


def handle_instrument(channel, pressed):
    global patch_index
    if pressed:
        patch_index += 1
        patch_index %= len(patches)
        print('Selecting Patch: {}'.format(patches[patch_index]))
        load_samples(patches[patch_index])


def handle_octave_up(channel, pressed):
    global octave
    if pressed and octave < octaves:
        octave += 1
        print('Selected Octave: {}'.format(octave))


def handle_octave_down(channel, pressed):
    global octave
    if pressed and octave > 0:
        octave -= 1
        print('Selected Octave: {}'.format(octave))


pianohat.on_note(handle_note)
pianohat.on_octave_up(handle_octave_up)
pianohat.on_octave_down(handle_octave_down)
pianohat.on_instrument(handle_instrument)

load_samples(patches[patch_index])

signal.pause()
