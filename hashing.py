import hashlib

def md5_hashing(text):
    md5 = hashlib.md5(text.encode('UTF-8'))
    return md5.hexdigest()

def sha1_hashing(text):
    sha1 = hashlib.sha1(text.encode('UTF-8'))
    return sha1.hexdigest()

def sha256_hashing(text):
    sha256 = hashlib.sha256(text.encode('UTF-8'))
    return sha256.hexdigest()

def sha512_hashing(text):
    sha512 = hashlib.sha512(text.encode('UTF-8'))
    return sha512.hexdigest()


def main():
    print()
    print("|--------------------------------|")
    print("|    Please Enter Hash Mode      |")
    print("|    Press 1 for MD5 Hashing     |")
    print("|    Press 2 for SHA1 Hashing    |")
    print("|    Press 3 for SHA256 Hashing  |")
    print("|    Press 4 for SHA512 Hashing  |")
    print("|    Press -1 to quit            |")
    print("|--------------------------------|")
    print()

    run = True
    while run:

        print()
        type = int(input("Enter choice: "))

        if type == -1:
            print()
            print("Thank you")
            print()
            run = False
        else:
            print()
            text = input("Enter text: ")


            if type == 1:
                print()
                print("MD5 Hashed value of your text:", md5_hashing(text))
            elif type == 2:
                print()
                print("SHA1 Hashed value of your text:", sha1_hashing(text))
            elif type == 3:
                print()
                print("SHA256 Hashed value of your text:", sha256_hashing(text))
            elif type == 4:
                print()
                print("SHA512 Hashed value of your text:", sha512_hashing(text))

if __name__ == "__main__":
    main()