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
    #print('MSG(HEX):',binascii.hexlify(input))
    try:
        msg = binascii.unhexlify(input)
        key = b'notsuchsecretkey' # 128 bit (16 bytes) key
        counter = "CC581687C248553B".encode() # hardware generated random IV (never reuse it)
        cipher = AES(key, AES.MODE_CTR, counter=counter)
        msg = cipher.encrypt(msg)
        print('Encrypted:',msg)
        print('Encrypted(HEX):',binascii.hexlify(msg))
        send(msg, s);
        pycom.rgbled(0x00FF00)  # Green
        uart.write('SENT')   # write the 3 characters
        time.sleep(2)

    except:
        pycom.rgbled(0xFF0000)  # Red
        time.sleep(2)
        break
