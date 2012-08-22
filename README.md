About
=====
Once started, PiFace Keymap will issue Linux uinput (keyboard/joystick)
events on PiFace input changes.

Dependencies
============
[python-uinput](http://tjjr.fi/sw/python-uinput/)

Usage
=====
Since we are issuing kernel level key presses, the program must be run with
root privelages:

    $ sudo python piface_keymap.py
