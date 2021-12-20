encoded = b"w1{1wq83k055j5f"

for i in range(len(encoded)):
    if i % 2 == 0:
        print(chr(encoded[i]-5), end='')
    else:
        print(chr(encoded[i]+2), end='')
