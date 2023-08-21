import hmac
import hashlib

def main():
    print("|--------------------------------|")
    print("|    Welcome to MAC generation   |")
    print("|--------------------------------|")
    print()

    run = True
    while run:
        message = input("Enter text: ").encode('UTF-8')
        print()

        key = input("Enter key: ").encode('UTF-8')
        print()

        print("|----------------------------------------|")
        print("|    Enter 1 For SHA-256 MAC Generation  |")
        print("|    Enter 2 For SHA-1 MAC Generation    |")
        print("|    Enter -1 to quit                    |")
        print("|----------------------------------------|")

        alg = int(input("Enter choice: "))

        if alg == 1:
            mac = hmac.new(key, message, hashlib.sha256)
            print("MAC: ", mac.hexdigest())
            print()

        elif alg == 2:
            mac = hmac.new(key, message, hashlib.sha1)
            print("MAC: ", mac.hexdigest())
            print()

        elif alg == -1:
            run = False
            print("Thank you")
            print()


if __name__ == "__main__":
    main()