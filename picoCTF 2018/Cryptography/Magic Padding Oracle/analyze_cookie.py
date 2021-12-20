all_bytes = input("Enter cookie: ")
print("Code length: " + str(len(all_bytes)))
for j in range(0, len(all_bytes), 32):
    print(all_bytes[j:j+32])
