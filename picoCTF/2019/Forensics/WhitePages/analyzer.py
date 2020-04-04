# Short program that converts the characters into ASCII to print the flag
with open("xdd_raw.txt", mode='r') as fin:
    file = fin.read()

for i in range(int(len(file) / 2)):
    c = file[i*2:i*2+2]
    # 0 pattern = '\xe2\x80\x83'
    # 1 pattern = ' '
    if c == "e2":
        # Start of a 0
        print(0, end='')
    elif c == "20":
        # Space, print 1
        print(1, end='')
    elif c == "80" or c == "83":
        # Known chars, don't print
        _ = 1
    else:
        # Print unknown chars
        print("\nUnknown: " + str(c))
