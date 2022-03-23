from sigfox_send import *
from crypto import AES
import crypto
from machine import UART
import pycom
import time
from network import Sigfox
import binascii

pycom.heartbeat(False)
# this uses the UART_1 non-default pins for TXD and RXD (``P20`` and ``P21``)
uart = UART(1, baudrate=9600, pins=('P10', 'P11'))
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ2)
s = init();
send(binascii.unhexlify("FFFFFFFFFFFFFFFFFFFFFFFF"), s);
time.sleep(2)

while(1):
    pycom.rgbled(0x0000FF)  # Blue
    while(1):
        if uart.any() > 0:
            break
    input = uart.read(uart.any()).decode()
    print('MSG:',input) # read up to 5 bytes
    print('MSG(HEX):',binascii.hexlify(input))
    msg = binascii.unhexlify(input)
    send(msg, s);
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(2)
