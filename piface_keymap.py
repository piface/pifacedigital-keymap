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
        elif not (input_bitp & 0x01) and first_key_pressed:
            # first input not pressed
            first_key_pressed = False
            device.emit(FIRST_KEY, 0) # Release

        if (input_bitp & 0x2) and not second_key_pressed:
            # second input pressed
            second_key_pressed = True
            device.emit(SECOND_KEY, 1) # Press
        elif not (input_bitp & 0x2) and second_key_pressed:
            # second input not pressed
            second_key_pressed = False
            device.emit(SECOND_KEY, 0) # Release

        if (input_bitp & 0x4) and not third_key_pressed:
            # third input pressed
            third_key_pressed = True
            device.emit(THIRD_KEY, 1) # Press
        elif not (input_bitp & 0x4) and third_key_pressed:
            # third input not pressed
            third_key_pressed = False
            device.emit(THIRD_KEY, 0) # Release

        if (input_bitp & 0x8) and not fourth_key_pressed:
            # fourth input pressed
            fourth_key_pressed = True
            device.emit(FOURTH_KEY, 1) # Press
        elif not (input_bitp & 0x8) and fourth_key_pressed:
            # fourth input not pressed
            fourth_key_pressed = False
            device.emit(FOURTH_KEY, 0) # Release

        if (input_bitp & 0x10) and not fifth_key_pressed:
            # fifth input pressed
            fifth_key_pressed = True
            device.emit(FIFTH_KEY, 1) # Press
        elif not (input_bitp & 0x10) and fifth_key_pressed:
            # fifth input not pressed
            fifth_key_pressed = False
            device.emit(FIFTH_KEY, 0) # Release

        if (input_bitp & 0x20) and not sixth_key_pressed:
            # sixth input pressed
            sixth_key_pressed = True
            device.emit(SIXTH_KEY, 1) # Press
        elif not (input_bitp & 0x20) and sixth_key_pressed:
            # sixth input not pressed
            sixth_key_pressed = False
            device.emit(SIXTH_KEY, 0) # Release

        if (input_bitp & 0x40) and not seventh_key_pressed:
            # seventh input pressed
            seventh_key_pressed = True
            device.emit(SEVENTH_KEY, 1) # Press
        elif not (input_bitp & 0x40) and seventh_key_pressed:
            # seventh input not pressed
            seventh_key_pressed = False
            device.emit(SEVENTH_KEY, 0) # Release

        if (input_bitp & 0x80) and not eighth_key_pressed:
            # eighth input pressed
            eighth_key_pressed = True
            device.emit(EIGHTH_KEY, 1) # Press
        elif not (input_bitp & 0x80) and eighth_key_pressed:
            # eighth input not pressed
            eighth_key_pressed = False
            device.emit(EIGHTH_KEY, 0) # Release

if __name__ == "__main__":
    main()
