from sigfox_send import *

from crypto import AES
import crypto
import ubinascii


key = b'notsuchsecretkey' # 128 bit (16 bytes) key
counter = "CC581687C248553B".encode() # hardware generated random IV (never reuse it)

cipher = AES(key, AES.MODE_CTR, counter=counter)
msg = cipher.encrypt(b'123456789012')
print(msg)
print(ubinascii.hexlify(msg))
print(len(msg))

s = init();
send(msg, s);
