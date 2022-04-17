from crypto import AES
import crypto
import binascii

key = b'notsuchsecretkey' # 128 bit (16 bytes) key
counter = "CC581687C248553B".encode() # hardware generated random IV (never reuse it)
print('Key',key)
print('Counter',counter)
#b'\xdd\xf1v\x06\x96\xa1w\x91l\x18"G}Xp\xbd'
cipher = AES(key, AES.MODE_CTR, counter=counter)
msg = cipher.encrypt(b'010217455045013DFF3D0000')
print('Encrypted MSG', msg)
print('Encrypted MSG(HEX):',binascii.hexlify(msg))
#b'\x18\xb4\x15X\xc2m\x9b0p\xdd\xb1\x9fgv'
#print(len(msg))
#counter = crypto.getrandbits(128)
# ... after properly sent the encrypted message somewhere ...
#counter = crypto.getrandbits(128) # hardware generated random IV (never reuse it)
cipher = AES(key, AES.MODE_CTR, counter=counter) # on the decryption side
original = cipher.decrypt(msg)
print('Decrypted MSG',original)
