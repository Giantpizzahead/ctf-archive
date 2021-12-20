out = ""
while True:
    part_in = input()
    if (part_in != 'q'):
        part_out = bytes.fromhex(part_in).decode()
        out += part_out[::-1]
    else:
        print(out)
        break
