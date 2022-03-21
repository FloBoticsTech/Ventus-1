from machine import UART
# this uses the UART_1 non-default pins for TXD and RXD (``P20`` and ``P21``)
uart = UART(1, baudrate=9600, pins=('P10', 'P11'))
i = 1
while i < 100000:
  i += 1


uart.write(b"hellolopy1")
print('Sent')
while(1):
    #uart.write(b"howdy")
    #print(uart.any())
    if uart.any() > 1:
        break
print(uart.read(uart.any())) # read up to 5 bytes
print(type(uart.read(uart.any()).decode()))
