#!/usr/bin/env python

import pianohat
import pygame
import time
import signal
import glob
import os
import re

import midi
import midi.sequencer

hw = midi.sequencer.SequencerHardware()

octave = 5
MIDI_CLIENT = -1
MIDI_PORT   = 0
START_PATCH = 1
BANK_SIZE   = 16

supported = ['yoshimi','SunVox']

for client in supported:
    if client in hw._clients:
        MIDI_CLIENT = hw._clients[client].client
        print('Connecting to {}'.format(client))
        break

if MIDI_CLIENT == -1:
    exit('Please install and run a supported client! :)')

class Piano():
    def __init__(self):
        self.current_patch = START_PATCH
        self.seq = midi.sequencer.SequencerWrite()
        self.seq.subscribe_port(MIDI_CLIENT, MIDI_PORT)
        self.seq.start_sequencer()
        self.select_patch(self.current_patch)
    
    def note_on(self, note, velocity=100):
        self.seq.event_write(midi.NoteOnEvent(velocity=velocity, pitch=note, tick=0), False, False, True)
        print("Note_on:{}".format(note))
    def note_off(self, note):
        self.seq.event_write(midi.NoteOffEvent(velocity=100, pitch=note, tick=0), False, False, True)
        print("Note_off:{}".format(note))

    def select_patch(self, patch):
        if patch < 0 or patch >= BANK_SIZE:
            raise ArgumentError("Invalid Patch")
        self.seq.event_write(midi.ProgramChangeEvent(tick=0, channel=0, data=[patch]), False, False, True)

    def next_patch(self):
        self.current_patch += 1
        self.current_patch %= BANK_SIZE
        self.select_patch(self.current_patch)

pianohat.auto_leds(True)
piano = Piano()

def handle_note(channel, pressed):
    velocity = 100
    if pressed:
        piano.note_on((octave * 12)  + channel, velocity)
    else:
        piano.note_off((octave * 12) + channel)

def handle_instrument(channel, pressed):
    piano.next_patch()

def handle_octave_up(channel, pressed):
    global octave
    if pressed:
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

signal.pause()
