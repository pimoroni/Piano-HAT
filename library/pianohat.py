#!/usr/bin/env python

import signal

try:
    import cap1xxx
except ImportError:
    exit("This library requires the cap1xxx module\nInstall with: sudo pip install cap1xxx")


_on_note        = None
_on_octave_up   = None
_on_octave_down = None
_on_instrument  = None

_pressed = [False for x in range(16)]

PRESSED  = True
RELEASED = False

C = 0
CSHARP = 1
D = 2
DSHARP = 3
E = 4
F = 5
FSHARP = 6
G = 7
GSHARP = 8
A = 9
ASHARP = 10
B = 11
C2 = 12

OCTAVE_DOWN = 13
OCTAVE_UP   = 14
INSTRUMENT  = 15

def _setup_cap(cap):
    for x in range(8):
        cap._write_byte(0x30 + x, 0b00000110)

    cap._write_byte(cap1xxx.R_LED_BEHAVIOUR_1, 0b00000000)
    cap._write_byte(cap1xxx.R_LED_BEHAVIOUR_2, 0b00000000)
    cap._write_byte(cap1xxx.R_LED_LINKING,     0b11111111)

    cap._write_byte(cap1xxx.R_SAMPLING_CONFIG, 0b00000000)
    cap._write_byte(cap1xxx.R_SENSITIVITY,     0b01100000)
    cap._write_byte(cap1xxx.R_GENERAL_CONFIG, 0b00111000)
    cap._write_byte(cap1xxx.R_CONFIGURATION2, 0b01100000)
    cap.set_touch_delta(10)
    cap.set_led_direct_ramp_rate(0,0)

def _handle_event(cap_index, event, state):
    global _pressed
    offset = 0
    if cap_index == 1: offset = 8
 
    channel = offset + event.channel

    _pressed[channel] = (state == PRESSED)
    
    if (channel) == OCTAVE_DOWN and callable(_on_octave_down):
        _on_octave_down(channel, state)
    if (channel) == OCTAVE_UP   and callable(_on_octave_up):
        _on_octave_up(channel, state)
    if (channel) == INSTRUMENT  and callable(_on_instrument):
        _on_instrument(channel, state)
    if (channel) <= 12 and callable(_on_note):
        _on_note(channel, state)

def auto_leds(enable = True):
    _piano_ctog._write_byte(cap1xxx.R_LED_LINKING, 0b11111111 * enable)
    _piano_atoc._write_byte(cap1xxx.R_LED_LINKING, 0b11111111 * enable)

def set_led(index, state):
    if index >= 8:
        _piano_atoc.set_led_state(index-8,state)
    else:
        _piano_ctog.set_led_state(index,state)

def set_led_ramp_rate(rise,fall):
    _piano_ctog.set_led_direct_ramp_rate(rise, fall)
    _piano_atoc.set_led_direct_ramp_rate(rise, fall)

def get_state(index=-1):
    if index > 0 and index < 16:
        return _pressed[index]
    else:
        return _pressed

def on_note(handler):
    global _on_note
    _on_note = handler

def on_octave_up(handler):
    global _on_octave_up
    _on_octave_up = handler

def on_octave_down(handler):
    global _on_octave_down
    _on_octave_down = handler

def on_instrument(handler):
    global _on_instrument
    _on_instrument = handler

# Keys C, C#, D, D#, E, F, F# and G
_piano_ctog = cap1xxx.Cap1188(i2c_addr=0x28, alert_pin=4)
_setup_cap(_piano_ctog)

# Keys G#, A, A#, B, C, Instrument, Octave -, Octave +
_piano_atoc = cap1xxx.Cap1188(i2c_addr=0x2b, alert_pin=27)
_setup_cap(_piano_atoc)

for x in range(0,8):
    _piano_ctog.on(x,event='press',  handler=lambda evt: _handle_event(0,evt,PRESSED ))
    _piano_ctog.on(x,event='release',handler=lambda evt: _handle_event(0,evt,RELEASED))
    _piano_atoc.on(x,event='press',  handler=lambda evt: _handle_event(1,evt,PRESSED ))
    _piano_atoc.on(x,event='release',handler=lambda evt: _handle_event(1,evt,RELEASED))

#_piano_ctog.clear_interrupt()
#_piano_atoc.clear_interrupt()
