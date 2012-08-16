#!/usr/bin/env python
"""
piface_keymap.py
Maps PiFace input changes to Linux uinput (keyboard/joystick) events.
"""
import piface.pfio as pfio
import uinput
from time import sleep


DELAY = 0.02

FIRST_KEY   = uinput.KEY_1
SECOND_KEY  = uinput.KEY_2
THIRD_KEY   = uinput.KEY_3
FOURTH_KEY  = uinput.KEY_4
FIFTH_KEY   = uinput.KEY_5
SIXTH_KEY   = uinput.KEY_6
SEVENTH_KEY = uinput.KEY_7
EIGHTH_KEY   = uinput.KEY_8


def main():
    events = (FIRST_KEY, SECOND_KEY, THIRD_KEY, FOURTH_KEY, FIFTH_KEY,
        SIXTH_KEY, SEVENTH_KEY, EIGHTH_KEY)
    device = uinput.Device(events)

    pfio.init()

    first_key_pressed   = False
    second_key_pressed  = False
    third_key_pressed   = False
    fourth_key_pressed  = False
    fifth_key_pressed   = False
    sixth_key_pressed   = False
    seventh_key_pressed = False
    eighth_key_pressed  = False

    while True:
        sleep(DELAY)

        input_bitp = pfio.read_input()

        if (input_bitp & 0x1) and not first_key_pressed:
            # first input pressed
            first_key_pressed = True
            device.emit(FIRST_KEY, 1) # Press
        elif first_key_pressed:
            # first input not pressed
            first_key_pressed = False
            device.emit(FIRST_KEY, 0) # Release

        if (input_bitp & 0x2) and not second_key_pressed:
            # second input pressed
            second_key_pressed = True
            device.emit(SECOND_KEY, 1) # Press
        else:
            # second input not pressed
            device.emit(SECOND_KEY, 0) # Release

        if input_bitp & 0x4:
            # third input pressed
            device.emit(THIRD_KEY, 1) # Press
        else:
            # third input not pressed
            device.emit(THIRD_KEY, 0) # Release

        if input_bitp & 0x8:
            # fourth input pressed
            device.emit(FOURTH_KEY, 1) # Press
        else:
            # fourth input not pressed
            device.emit(FOURTH_KEY, 0) # Release

        if input_bitp & 0x10:
            # fifth input pressed
            device.emit(FIFTH_KEY, 1) # Press
        else:
            # fifth input not pressed
            device.emit(FIFTH_KEY, 0) # Release

        if input_bitp & 0x20:
            # sixth input pressed
            device.emit(SIXTH_KEY, 1) # Press
        else:
            # sixth input not pressed
            device.emit(SIXTH_KEY, 0) # Release

        if input_bitp & 0x40:
            # seventh input pressed
            device.emit(SEVENTH_KEY, 1) # Press
        else:
            # seventh input not pressed
            device.emit(SEVENTH_KEY, 0) # Release

        if input_bitp & 0x80:
            # eighth input pressed
            device.emit(EIGHTH_KEY, 1) # Press
        else:
            # eighth input not pressed
            device.emit(EIGHTH_KEY, 0) # Release

if __name__ == "__main__":
    main()
