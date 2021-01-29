enc1 = []
with open("enc1", 'rb') as fin:
    enc1 = [hex(x)[2:] for x in fin.read()]
enc2 = []
with open("enc2", 'rb') as fin:
    enc2 = [hex(x)[2:] for x in fin.read()]

print(len(enc1))
print(len(enc2))
# for i in range(len(enc1)):
#     print(hex(enc1[i] ^ enc2[i])[2:], end='')
print(''.join(enc1))
print()
print(''.join(enc2))