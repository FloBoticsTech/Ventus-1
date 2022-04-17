from machine import UART
import binascii

# this uses the UART_1 non-default pins for TXD and RXD (``P20`` and ``P21``)
uart = UART(1, baudrate=9600, pins=('P10', 'P11'))
##i = 1
#while i < 100000:
#  i += 1


#uart.write(b"FFFFFFFFFFFFFFFFFFFFFFFF")
print('Sent')
#in = "Howdy"
uart.write("010117455045013DFF3D0000")
