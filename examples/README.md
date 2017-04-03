Piano HAT will work with anything that supports MIDI input, thanks to Python MIDI and the `midi-piano.py` example.

## Installing Python MIDI

This is a little tricky, but if you follow these steps you should get it installed in no time:

First you'll need some dependencies, install them with:

```bash
sudo apt-get install python-dev libasound2-dev swig
```

Next, you need to clone the following GitHub repo:

```bash
git clone https://github.com/vishnubob/python-midi`
cd python-midi && sudo ./setup.py install
```

If it installs properly, you should get a handy new tool `mididumphw.py` which will tell you what MIDI-compatible synths you've got running and what Client/Port IDs you'll need to connect to to use them.

## Using `midi-piano.py`

By default the MIDI Piano example supports SunVox and yoshimi:

* Sunvox ( Get it from http://www.warmplace.ru/soft/sunvox/ )
* Yoshimi ( `sudo apt-get install yoshimi` )

Run either of these synths first, and then run `sudo ./midi-piano.py` and start playing.

For best results, you should use a Pi 2/3, especially with Yoshimi which can be a bit taxing on the older models or Pi Zero.
