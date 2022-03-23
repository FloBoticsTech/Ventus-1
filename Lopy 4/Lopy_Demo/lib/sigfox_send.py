from network import Sigfox
import socket
import struct
import pycom
import time

def init():
    # init Sigfox for RCZ2 (USA)
    sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2)

    # create a Sigfox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

    # make the socket blocking
    s.setblocking(True)
    s.settimeout(60)
    return s


def change_led(v):
    pycom.heartbeat(False)

    while True:
        #colors in hexadecimal (0xRRGGBB)
        pycom.rgbled(0xFF0000)  # Red
        time.sleep(1)
        pycom.rgbled(0x00FF00)  # Green
        time.sleep(1)
        pycom.rgbled(0x0000FF)  # Blue
        time.sleep(1)


def send_and_receive(msg):
    # configure it as both ways link
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)
    try:
        s.send(msg)
    except OSError as e:
        print('error in send...', e)
    else:
        response = s.recv(64)
        change_led(response)
        return response


def send(msg, s):
    # configure it uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
    return s.send(msg)


# stop led heartbeat
pycom.heartbeat(True)
