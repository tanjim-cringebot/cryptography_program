from prompt_toolkit import key_binding
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def cbc_encryption(text, key):
    iv = get_random_bytes(AES.block_size)
    encryption_cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + encryption_cipher.encrypt(pad(text, AES.block_size)))

def cbc_decryption(text, key):
    raw = b64decode(text)
    decryption_cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(decryption_cipher.decrypt(raw[AES.block_size:]), AES.block_size)


def ecb_encryption(text, key):
    text = pad(text, 16)
    encryption_cipher = AES.new(key, AES.MODE_ECB)
    return b64encode(encryption_cipher.encrypt(text))


def ecb_decryption(text, key):
    text = b64decode(text)
    decryption_cipher = AES.new(key, AES.MODE_ECB)
    return unpad(decryption_cipher.decrypt(text), 16)


def main():
    print()
    print("|----------------------------|")
    print("|    Please Enter AES Mode   |")
    print("|    Press 1 for CBC         |")
    print("|    Press 2 for ECB         |")
    print("|    Press -1 to quit        |")
    print("|----------------------------|")
    print()

    run = True
    while run:
        chos = int(input("Enter choice: "))
        print()

        if chos == 1:
            print()
            print("|----------------------------|")
            print("|    Please Enter Operation  |")
            print("|    Press 1 for Encryption  |")
            print("|    Press 2 for Decryption  |")
            print("|----------------------------|")
            print()

            enc_dec = int(input("Enter encryption/decryption: "))

            if enc_dec == 1:
                text = input("Enter text: ").encode('UTF-8')

                key = input("Enter key: ")
                key = md5(key.encode('UTF-8')).digest()
                print()

                encrypt = cbc_encryption(text, key)
                print("Encryption: ", encrypt)

            elif enc_dec == 2:
                decrypt = input("Enter text: ")

                key = input("Enter key: ")
                key = md5(key.encode('UTF-8')).digest()
                print()

                decrypt = cbc_decryption(decrypt, key)
                print("Decryption: ", decrypt.decode('UTF-8'))

        if chos == 2:
            print()
            print("|----------------------------|")
            print("|    Please Enter Operation  |")
            print("|    Press 1 for Encryption  |")
            print("|    Press 2 for Decryption  |")
            print("|----------------------------|")
            print()

            enc_dec = int(input("Enter encryption/decryption: "))

            if enc_dec == 1:
                text = input("Enter text: ").encode('UTF-8')
                print()

                key = input("Enter key: ")
                key = md5(key.encode('UTF-8')).digest()
                print()

                encrypt = ecb_encryption(text, key)
                print("Encrypted text:", encrypt.decode('UTF-8', 'ignore'))
                print()

            elif enc_dec == 2:
                encrypt = input("Enter text: ")
                print()

                key = input("Enter key: ")
                key = md5(key.encode('UTF-8')).digest()
                print()

                decrypt = ecb_decryption(encrypt, key)
                print(decrypt.decode('UTF-8', 'ignore'))
                print()

        elif chos == -1:
            run = False
            print("Thank you")
            print()


if __name__ == "__main__":
    main()