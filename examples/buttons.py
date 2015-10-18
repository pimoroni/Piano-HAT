#!/usr/bin/env python
print("""
This simple example shows you how to make Piano HAT keypresses do something useful.

You should see details of each press appear below as you touch Piano HAT's keys

Press CTRL+C to exit.
""")
import pianohat
import signal

pianohat.auto_leds(True)

def handle_touch(ch, evt):
    print(ch, evt)

pianohat.on_note(handle_touch)
pianohat.on_octave_up(handle_touch)
pianohat.on_octave_down(handle_touch)
pianohat.on_instrument(handle_touch)

signal.pause()
