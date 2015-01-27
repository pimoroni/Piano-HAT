#!/usr/bin/env python

import RPi.GPIO as GPIO
import smbus
bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)

ADDRA = 0x28
ADDRB = 0x2b

INPUT_CONFIG_REG  = 0x22
INPUT_CONFIG_REG2 = 0x23
MULTI_TOUCH_REG   = 0x2A
LED_LINK_REG      = 0x72
LED_BEHAVE_1      = 0x81
LED_BEHAVE_2      = 0x82
MULTI_TOUCH_PAT   = 0x2b


buttons = {
ADDRA:
{
1:  'C',
2:  'C#',
4:  'D',
8:  'D#',
16: 'E',
32: 'F',
64: 'F#',
128:'G'
},
ADDRB:
{
1:   'G#',
2:   'A',
4:   'A#',
8:   'B',
16:  'C',
32:  'DRUMS',
64:  'STRINGS',
128: 'PIANO'
}
}

for pin in [17,22]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for cap in [ADDRA, ADDRB]:
    bus.write_byte_data(cap, INPUT_CONFIG_REG,  0b10100000)
    bus.write_byte_data(cap, INPUT_CONFIG_REG2, 0b00000000)
    bus.write_byte_data(cap, MULTI_TOUCH_REG,   0b10000000)

    bus.write_byte_data(cap, MULTI_TOUCH_PAT,   0b10000100)

    bus.write_byte_data(cap, LED_BEHAVE_1, 0b00000000)
    bus.write_byte_data(cap, LED_BEHAVE_2, 0b00000000)
    bus.write_byte_data(cap, LED_LINK_REG, 0x11111111)
    #bus.write_byte_data(cap, 0x77, 0b00000000)
    #bus.write_byte_data(cap, 0x44, 0b11000000)

    for thresh in [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]:
        bus.write_byte_data(cap, thresh, 0b01000000)

while True:
    try:
        for cap in [ADDRA, ADDRB]:
            int = bus.read_byte_data(cap,0)
            if int & 1:
                touched = bus.read_byte_data(cap,3)
                bus.write_byte_data(cap,0,0)
                for id, button in buttons[cap].iteritems():
                    if touched & id:
                        print(button)

    except IOError:
        print("IOError?")
