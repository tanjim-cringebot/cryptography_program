from hashlib import md5

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = input("Enter key: ")
key = md5(key.encode('UTF-8')).digest()

def cbc_encryption(text):
    iv = get_random_bytes(AES.block_size)
    encryption_cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + encryption_cipher.encrypt(pad(text, AES.block_size))

def cbc_decryption(text):
    raw = text[:AES.block_size]
    decryption_cipher = AES.new(key, AES.MODE_CBC, raw)
    return unpad(decryption_cipher.decrypt(text[:AES.block_size:]), AES.block_size)

def ecb_encryption(text):
    encryption_cipher = AES.new(key, AES.MODE_ECB)
    return encryption_cipher.encrypt(pad(text, AES.block_size))

def ecb_decryption(text):
    raw = text[:AES.block_size]
    decryption_cipher = AES.new(key, AES.MODE_ECB, raw)
    return unpad(decryption_cipher.decrypt(text[AES.block_size:]), AES.block_size)

text = input("Enter text: ").encode('UTF-8')

encrypt = cbc_encryption(text)
print(encrypt)

decrypt = cbc_decryption(encrypt).decode('UTF-8')
print(decrypt)
