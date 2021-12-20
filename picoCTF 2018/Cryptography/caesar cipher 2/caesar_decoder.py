'''
Kinda retrieves the flag from the ciphertext. The cases are switched, and
the brackets / underscores aren't right, but it was enough to get the flag.
(Question marks are underscores)
'''

CIPHERTEXT = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"

minsofar = 9999
for c in CIPHERTEXT:
    minsofar = min(ord(c), minsofar)

print(minsofar)
'''
# Try every possible shift
for shift in range(-20, 50):
    newtext = ""
    for c in CIPHERTEXT:
        newtext += chr(ord(c) + shift)
    print(str(shift) + ": " + newtext)
'''

ALPHABET = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{|}~"""
ALPHABET += ALPHABET


newtext = ""
for c in CIPHERTEXT:
    if ord(c) < 65:
        newtext += ALPHABET[ALPHABET.find(c) + 28]
    elif ord(c) > 96 and ord(c) < 123:
        newtext += ALPHABET[ALPHABET.find(c) - 2]
print("Old: " + CIPHERTEXT)
print("New: " + newtext)
