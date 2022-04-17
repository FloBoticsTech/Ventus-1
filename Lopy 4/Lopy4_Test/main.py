from sigfox_send import *

from crypto import AES
import crypto
import ubinascii


key = b'notsuchsecretkey' # 128 bit (16 bytes) key
counter = "CC581687C248553B".encode() # hardware generated random IV (never reuse it)

cipher = AES(key, AES.MODE_CTR, counter=counter)
temp = 0xFFFFFFFFFFFF
#print(int(temp, 2))
msg = binascii.unhexlify('FFFFFFFFFFFFFFFFFFFFFFFF')
msg_new = 'Howdy'
en_msg = cipher.encrypt(msg_new)
print(msg)
print(ubinascii.hexlify(msg))
print(len(msg))
print(en_msg)
new = ubinascii.hexlify(en_msg)
print(new)
print(binascii.unhexlify(new))

s = init();
#send(msg, s);
#send(en_msg, s);
