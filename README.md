#Piano HAT

* 16 Capacitive Touch Buttons
* 13 Notes from C to C
* Octave Up/Down
* Instrument Select

#Using Piano HAT

Piano HAT will work with anything that supports MIDI input, thanks to Python MIDI and the `midi-piano.py` example.

##Installing Python MIDI

This is a little tricky, but if you follow these steps you should get it installed in no time:

First you'll need some dependencies, install them with: `sudo apt-get install python-dev libasound2-dev swig`

Next, you need to clone the GitHub repo: `git clone https://github.com/vishnubob/python-midi`

And install it: `cd python-midi && sudo ./setup.py install`

If it installs properly, you should get a handy new tool `mididumphw.py` which will tell you what MIDI-compatible synths you've got running and what Client/Port IDs you'll need to connect to to use them.

##Using `midi-piano.py`

You'll find the MIDI Piano example in the examples folder of this repository, or in `~/Pimoroni/piano-hat` if you used our installer script. By default it supports SunVox and yoshimi:

* Sunvox ( Get it from http://www.warmplace.ru/soft/sunvox/ )
* Yoshimi ( `sudo apt-get install yoshimi` )

Run either of these synths first, and then run `sudo ./midi-piano.py` and start playing.
