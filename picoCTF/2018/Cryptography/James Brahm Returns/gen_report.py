while True:
    report = input("Enter the report: ")
    if report == 'q': exit(0)
    #report = '0'*11 + report + '0'*((16 * (len(report) // 16 + 1) - len(report)) + 1)
    print(report)
    added = input("Anything to add: ")

    message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {2}.
Down with the Soviets,
006
{1}hashhashhashhashhash""".format(report, added, "picoCTF{abcdefghijklmnopqrstuvwxyz0123456789}")

    if len(message) % 16 != 0:
        message += '0'*(16 - len(message) % 16)
    else:
        message += '0'*16

    all_bytes = input("Enter response: ")

    print("Message length: " + str(len(message)))
    print("Code length: " + str(len(all_bytes)))
    j = 0
    for i in range(0, len(message), 16):
        print(message[i:i+16] + " = " + all_bytes[j:j+32])
        j += 32
