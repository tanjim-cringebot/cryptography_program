def mod_inverse(x, y):
  i = pow(x, -1, y)
  return i

def gcd(a, b):
    while b != 0:
        a = b
        b = a % b
    return a

def encryption(m, e, n):
    ciphertext = (m**e) % n
    return ciphertext

def decryption(c, d, n):
    message = (c**d) % n
    return message



def main():
    print()
    print("|----------------------------|")
    print("|    Please Enter RSA Mode   |")
    print("|    Press 1 for Encryption  |")
    print("|    Press 2 for Decryption  |")
    print("|    Press -1 to quit        |")
    print("|----------------------------|")
    print()

    run = True
    while run:
        choice = int(input("Enter choice: "))
        print()

        if choice == 1:
            p = int(input("Enter the value of P: "))
            print()

            q = int(input("Enter the value of Q: "))
            print()
            
            n = p*q
            phi = (p - 1) * (q - 1)

            e = int(input("Enter the value of E(1 < e < phi; gcd(e, phi) != 1): "))
            print()

            m = int(input("Enter message: "))
            print()

            print("Encrypted text: ", encryption(m , e, n))
            print()
        
        elif choice == 2:
            p = int(input("Enter the value of P: "))
            print()

            q = int(input("Enter the value of Q: "))
            print()

            e = int(input("Enter the value of E(1 < e < phi; gcd(e, phi) != 1): "))
            print()
            
            n = p*q
            phi = (p - 1) * (q - 1)
            
            d = mod_inverse(e, phi)

            c = int(input("Enter ciphertext: "))
            print()

            print("Decrypted text: ", decryption(c, d, n))
            print()
        
        elif choice == -1:
            run = False
            print("Thank You")
            print()


if __name__ == "__main__":
    main()