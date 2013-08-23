About
=====
PiFace Keymap will issue uinput (keyboard/joystick) events on PiFace Digital
input events.

python-uinput
=============
python-uinput is required for this program to work. There is no clean way of
installing this on Debian as of yet. The cleanest way I have found is:

    sudo apt-get install libudev-dev python-all-dev
    git clone https://github.com/tuomasjjrasanen/python-uinput.git
    cd python-uinput/
    sudo python setup.py install

I have created an [issue](https://answers.launchpad.net/python-uinput/+question/234455)
asking where the Debian packages are. Hopefully there will be a cleaner
installation eventually.

Also, for `python-uinput` to work you will have to load the `uinput` kernel
module:

    sudo modprobe uinput

You can permenantly enable this by adding `uinput` to `/etc/modules`

    sudo echo uinput >> /etc/modules

Use
===
Since we are issuing kernel level key presses and we haven't done a clean
installation, the program must be run with root privelages:

    $ sudo python pifacedigital_keymap.py

The events emitted on inputs 0-7 are defined as:

    UNINPUT_EVENTS = (
        uinput.KEY_1,  # 0
        uinput.KEY_2,
        uinput.KEY_3,
        uinput.KEY_4,
        uinput.KEY_5,
        uinput.KEY_6,
        uinput.KEY_7,
        uinput.KEY_8,  # 7
    )

Change these in the code to emit different keyboartd events. You can find a
list of them in `/usr/include/linux/input.h`.
