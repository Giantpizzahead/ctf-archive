while True:
    mode = input("Mode? ([a]nalyze, [j]oin) ")

    if mode == 'a':
        # Analyze
        all_bytes = input("Enter cookie: ")
        print("Code length: " + str(len(all_bytes)))
        for j in range(0, len(all_bytes), 32):
            print(all_bytes[j:j+32])
    elif mode == 'j':
        # Join
        out = ""
        print("Paste the whole cookie. q to stop at the end.")
        while True:
            nextline = input()
            if nextline == 'q': break
            out += nextline
        print(out)
    else:
        quit()
