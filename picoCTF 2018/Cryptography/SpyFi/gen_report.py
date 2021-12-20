while True:
    report = input("Enter the report: ")
    if report == 'q': exit(0)
    #report = '0'*11 + report + '0'*((16 * (len(report) // 16 + 1) - len(report)) + 1)
    print(report)

    message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format(report, "picoCTF{abcdefghijklmnopqrstuvwxyz}")

    if len(message) % 16 != 0:
        message += '0'*(16 - len(message) % 16)

    all_bytes = input("Enter response: ")

    print("Message length: " + str(len(message)))
    print("Code length: " + str(len(all_bytes)))
    j = 0
    for i in range(0, len(message), 16):
        print(message[i:i+16] + " = " + all_bytes[j:j+32])
        j += 32
