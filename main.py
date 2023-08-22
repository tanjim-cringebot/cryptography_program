import subprocess

aes_file = 'aes.py'
rsa_file = 'rsa.py'
mac_file = 'mac.py'
hash_file = 'hashing.py'
sign_file = 'signature.py'

def main():
    print()
    print("|----------------------------------------------------|")
    print("|    Welcome to Cryptography Project                 |")
    print("|----------------------------------------------------|")
    print("|    Enter your preferable operation                 |")
    print("|    Enter 1 to perform AES Encryption/Decryption    |")
    print("|    Enter 2 to perform RSA Encryption/Decryption    |")
    print("|    Enter 3 to perform Hashing                      |")
    print("|    Enter 4 to perform Digital Signature using RSA  |")
    print("|    Enter 5 to perform MAC Generation               |")
    print("|    Enter -1 to EXIT                                |")
    print("|----------------------------------------------------|")
    print()

    run = True
    while run:
        task = int(input("Enter algorithm: "))

        if task == 1:
            subprocess.run(['python', aes_file])
        elif task == 2:
            subprocess.run(['python', rsa_file])
        elif task == 3:
            subprocess.run(['python', hash_file])
        elif task == 4:
            subprocess.run(['python', sign_file])
        elif task == 5:
            subprocess.run(['python', mac_file])
        elif task == -1:
            run = False
            print("THANK YOU!!!!")
            print()

if __name__ == "__main__":
    main()