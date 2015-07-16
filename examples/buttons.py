#!/usr/bin/env python

import pianohat
import time
import signal

pianohat.auto_leds(True)

def handle_touch(ch, evt):
    print(ch, evt)

pianohat.on_note(handle_touch)
pianohat.on_octave_up(handle_touch)
pianohat.on_octave_down(handle_touch)
pianohat.on_instrument(handle_touch)

signal.pause()
