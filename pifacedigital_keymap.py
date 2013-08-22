import time
import uinput
import pifacedigitalio


# uinput events for PiFace Digital inputs 0-7
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


def input_pressed(event):
    global device
    device.emit(UNINPUT_EVENTS[event.pin_num], 1)


def input_unpressed(event):
    global device
    device.emit(UNINPUT_EVENTS[event.pin_num], 0)


if __name__ == "__main__":
    pifacedigitalio.init()
    global device
    device = uinput.Device(UNINPUT_EVENTS)
    listener = pifacedigitalio.InputEventListener()
    for i in range(8):
        listener.register(i, pifacedigitalio.IODIR_ON, input_pressed)
        listener.register(i, pifacedigitalio.IODIR_OFF, input_unpressed)
    listener.activate()
