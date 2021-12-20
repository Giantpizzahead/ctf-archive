while True:
    mode = input("Mode? ([a]nalyze, [j]oin) ")

    if mode == 'a':
        # Analyze
        all_bytes = input("Enter ciphertext: ")
        print("Code length: " + str(len(all_bytes)))
        print("Num blocks: " + str(len(all_bytes) // 32))
        print("Plaintext length (plus padding): " + str(len(all_bytes) // 32 * 16))
        for j in range(0, len(all_bytes), 32):
            print(str(j//32+1) + ":", all_bytes[j:j+32])
    elif mode == 'j':
        # Join
        out = ""
        print("Paste the whole ciphertext. q to stop at the end.")
        while True:
            nextline = input()
            if nextline == 'q': break
            out += nextline
        print(out)
    elif mode == 'q':
        exit()
