About
=====
Once started, PiFace Keymap will issue Linux uinput (keyboard/joystick)
events on PiFace input changes.

Dependencies
============
Download the latest version of [python-uinput](http://tjjr.fi/sw/python-uinput/) (0.8 at the time of writing) and install it.

    $ wget https://launchpad.net/python-uinput/trunk/0.8/+download/python-uinput-0.8.tar.gz
    $ tar -xvf python-uinput-0.8.tar.gz
    $ cd python-uinput-0.8/
    $ sudo python setup.py install

Usage
=====
Since we are issuing kernel level key presses, the program must be run with
root privelages:

    $ sudo python piface_keymap.py
