# For picoCTF
# Note: This was made on the spot, so it might be inefficient. Also, the code
# doesn't really do anything useful.
import binascii

def printchars(y):
    a = input("#s ").split()
    for i in a:
        b = int(i, int(y))
        x = binascii.unhexlify('%x' % b)
        print(x)

while True:
    printchars(input("Base "))
