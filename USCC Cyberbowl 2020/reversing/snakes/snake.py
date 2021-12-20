def get_me_the_stuff(secretz):
    return ''.join([chr(c - len(secretz) + 1 ^ secretz[0]) for c in secretz[1:]])


codez = [87, 33, 35, 51, 51, 75, 35, 88, 85, 91, 81, 135, 39, 35, 88, 85, 91, 81, 149, 135, 39, 35, 88, 85, 85, 85, 85, 85, 91, 81, 149, 73]

print(get_me_the_stuff(codez))