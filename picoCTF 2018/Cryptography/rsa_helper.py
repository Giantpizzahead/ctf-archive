"""
A tool to help with all your RSA encryption needs.
Made for picoCTF.
"""
import math

PUBLIC_KEY = -1
EXPONENT = -1
PRIME_1 = -1
PRIME_2 = -1
PRIVATE_KEY = -1
CIPHER_TEXT = -1


def main():
    print(small_exponent_exploit())


# --- RSA Functions ---


def private_key_from_primes(p1, p2, e):
    """
    Calculates the private key from the two known primes, and a given exponent.
    """
    totient = (p1 - 1) * (p2 - 1)
    print("Totient: " + str(totient))
    private_key = mod_inv(e, totient)
    print("Private key: " + str(private_key))
    return private_key


def encrypt(public_key, exponent, text):
    """
    Encrypts the text, given the public key and the exponent.
    """
    return pow(text, exponent, public_key)


def decrypt(public_key, private_key, cipher_text):
    """
    Decrypts the cipher text, given the public and private keys.
    """
    return pow(cipher_text, private_key, public_key)


# --- Exploit-related ---


def small_exponent_exploit():
    print("Attempting to exploit a small exponent...")
    root = precise_root(CIPHER_TEXT, EXPONENT)
    print("Result: " + num_to_text(root))


def brute_force_private_key(public_key, cipher_text):
    print("Attempting to brute force the private key...")
    curr_cipher = cipher_text
    private_key = 1
    while True:
        text = num_to_text(curr_cipher)
        if "picoCTF{" in text:
            print("Text decrypted!")
            print("Private key: " + str(private_key))
            print("Decrypted text: " + text)
            break
        if private_key % 100000 == 0:
            print("On private key " + str(private_key))
        private_key += 1
        curr_cipher *= cipher_text
        curr_cipher %= public_key
    return private_key


def precise_root(num, root):
    """
    Uses binary search to find the precise root of a number.
    Useful when the exponent value is very small, and the cipher
    text is very short (not big enough to get moduloed).
    """
    lower = 0
    upper = round(num ** (1 / (EXPONENT // 1.5))) + 1
    while lower <= upper:
        middle = (lower + upper) // 2
        test_cube = middle ** root
        if test_cube < num:
            # Number too low
            lower = middle + 1
        elif test_cube > num:
            # Number too high
            upper = middle - 1
        else:
            # Found exact root
            print("Exact root: " + str(middle))
            return middle

    # No exact root found; return the best of lower and upper
    print("No exact root")
    # print(lower, upper)
    if abs(lower ** root - num) < abs(upper ** root - num):
        return lower
    else:
        return upper


# --- Other Useful Functions ---


def num_to_text(num):
    """
    Converts a number message into a text message.
    """
    num_to_hex = str(hex(num))
    text = ''
    for i in range(2, len(num_to_hex), 2):
        text += chr(int(num_to_hex[i:i+2], 16))
    return text


# --- Functions from online ---


def e_gcd(a, b):
    """
    Source: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = e_gcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a, m):
    """
    Source: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    """
    g, x, y = e_gcd(a, m)
    if g != 1:
        raise Exception("No modular inverse found for {0} and {1]".format(a, m))
    else:
        return x % m


if __name__ == "__main__":
    main()
