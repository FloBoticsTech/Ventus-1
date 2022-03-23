import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
def int_of_string(s):
    return int(binascii.hexlify(s), 16)
def encrypt_message(iv, key, plaintext):
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.encrypt(plaintext)
def decrypt_message(iv, key, ciphertext):
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext)

key = b'notsuchsecretkey'
msg = b'Attack at dawn'
iv = b'\xdd\xf1v\x06\x96\xa1w\x91l\x18"G}Xp\xbd'
en_msg = encrypt_message(iv, key, msg)
print(en_msg)
print(len(en_msg))
de_msg = decrypt_message(iv, key, en_msg)
print(de_msg)

#part2
iv = b'7280336e1f644015'
print(iv)
msg = b'123456789012'
en_msg = encrypt_message(iv, key, msg)
print(en_msg)
print(len(en_msg))
data = b'110694b7b6204d4aeaa5fb06'
de_data = (binascii.unhexlify(data))
de_data = decrypt_message(iv, key, de_data)
print(de_data)