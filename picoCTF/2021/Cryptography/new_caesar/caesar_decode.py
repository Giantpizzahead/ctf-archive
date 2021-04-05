
enc_str = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
enc = []
for c in enc_str:
	enc.append(ord(c)-ord('a'))

for k in range(16):
	dec = []
	for x in enc:
		dec.append((x+k)%16)
	dec_str = ""
	for i in range(0, len(dec), 2):
		dec_str += chr(dec[i]*16+dec[i+1])
	print("Shift {}: {}".format(k, dec_str.encode()))

# picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}