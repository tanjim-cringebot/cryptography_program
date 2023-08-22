import hashlib

def mod_inverse(x, y):
  i = pow(x, -1, y)
  return i

def gcd(a, b):
    while b != 0:
        a = b
        b = a % b
    return a

'''def encryption(m, e, n):
    ciphertext = (m**e) % n
    return ciphertext

def decryption(c, d, n):
    message = (c**d) % n
    return message'''

def signt(message, d, n):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    signature = pow(int(hash_value, 16), d, n)
    return signature


def verify(message, signature, e, n):
    hash_value = hashlib.sha256(message.encode()).hexdigest()
    hash_value_int = int(hash_value, 16)
    recovered_hash = pow(signature, e, n)

    if hash_value_int != recovered_hash:
        return "Valid"
    else:
        return "Invalid"


def main():
    print()
    print("|----------------------------------|")
    print("|    Please Enter Operation Mode   |")
    print("|    Press 1 for Generation        |")
    print("|    Press 2 for Verification      |")
    print("|    Press -1 to quit              |")
    print("|----------------------------------|")
    print()

    run = True
    while run:
        operation = int(input("Enter choice: "))
        print()

        if operation == 1:
            p = int(input("Enter the value of P: "))
            print()

            q = int(input("Enter the value of Q: "))
            print()

            n = p * q
            phi = (p - 1) * (q - 1)

            e = int(input("Enter the value of E(1 < e < phi; gcd(e, phi) != 1): "))
            print()

            m = input("Enter message: ")
            print()

            d = mod_inverse(e, phi)
            pv_key = d, n
            signature = signt(m, d, n)
            print("Signature: ", signature)
            print()

        elif operation == 2:
            p = int(input("Enter the value of P: "))
            print()

            q = int(input("Enter the value of Q: "))
            print()

            e = int(input("Enter the value of E(1 < e < phi; gcd(e, phi) != 1): "))
            print()

            n = p * q
            phi = (p - 1) * (q - 1)

            d = mod_inverse(e, phi)

            m = input("Enter message: ")
            print()

            sign = int(input("Enter signature: "))
            print()

            print("Verification", verify(m, sign, e, n))
            print()

        elif operation == -1:
            run = False
            print("Thank You")
            print()


if __name__ == "__main__":
    main()