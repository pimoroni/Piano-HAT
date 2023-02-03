![Piano HAT](piano-hat-logo-new.png)
https://shop.pimoroni.com/products/piano-hat

Piano HAT is a tiny Pi piano with 16 touch-sensitive buttons. It features:

* 16 Capacitive Touch Buttons
* 13 Notes from C to C
* Octave Up/Down
* Instrument Select

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Piano HAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/pianohat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/pianohat/`.

⚠ Note that on recent versions of Raspberry Pi OS, you may need to **enable I2C manually**. You can do this using the Raspberry Pi Configuration utility - find it in the 'Preferences' menu, or enter `sudo raspi-config` at a Terminal prompt. The option to enable I2C is under 'Interfaces'.

### Manual install:

#### Library install for Python 3:

on Raspberry Pi OS:

```bash
sudo apt install python3-pianohat
```

other environments: 

```bash
python3 -m pip install pianohat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/
* Function reference - http://docs.pimoroni.com/pianohat/
* GPIO Pinout - https://pinout.xyz/pinout/piano_hat
* Get help - http://forums.pimoroni.com/c/support
