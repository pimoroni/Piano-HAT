# Piano HAT Function Reference

This library lets you use Piano HAT in Python to control whatever project you might assemble.

See `buttons.py` for an example of how to handle buttons. The library has 4 different events you can bind to:

* `on_note` - triggers when a piano key is touched
* `on_octave_up` - triggers when the Octave Up key is touched
* `on_octave_down` - triggers when the Octave Down key is touched
* `on_instrument` - triggeres when the Instrument key is touched

See `leds.py` for an example of how to take command of the Piano HAT LEDs. You can turn all of the LEDs on and off at will, useful for creating a visual metronome, prompting a user which key to press and more.

* `set_led(x, True/False)` - lets you set a particular LED to on ( True ) or off ( False ).
* `auto_leds(False)` - stops Piano HAT from automatically lighting the LEDs when a key is touched
