"""
Gets the flag for the "James Brahm Returns" picoCTF challenge when run.
Uses a modified version of the padding oracle exploit (POODLE vulnerability for SSLv3).
This takes quite a while to run, so I wouldn't recommend doing that.
"""

import socket
import time

SERVER = "2018shell.picoctf.com"
PORT = 15596
BUFFER_SIZE = 4096
DEBUG = True
DEBUG_LOW = False
s = socket.socket()
s.settimeout(3)


def main():
    start_connection()
    known = "picoCTF{g0_@g3nt006!_9101447}"
    starti = 21

    # Main loop
    for i in range(starti, 21):
        print("The flag so far: " + known)
        if DEBUG:
            print("Current index:", i)
        report, added = generate_reports(i)
        while True:
            plaintext_byte = brute_force_byte(report, added)
            if plaintext_byte is not None:
                break
        if DEBUG:
            print("Found new byte:", plaintext_byte)
        known += chr(plaintext_byte)

    # Print the answer
    print("------------------------------------------------------------")
    print("The flag is:")
    print(known + "}")


def brute_force_byte(report, added):
    """
    Brute forces an unknown byte in the flag. Makes 512
    requests on average per byte.
    """
    attempt = 1
    if DEBUG:
        print("Attempt # ", end='')
    while True:
        cipher_text = query_encrypt(report, added)
        # Replace last block of cipher_text with block #10 (9 with zero indexing)
        cipher_text = cipher_text[:-33] + get_block(cipher_text, 9)

        # Check if the byte is correct by querying server for decryption
        result = query_decrypt(cipher_text)
        if DEBUG_LOW:
            print("Attempt", attempt)
        elif DEBUG:
            print(attempt, end=' ')
        if "Successful decryption." in result:
            # It worked! Figure out the value of the original plaintext byte, then exit
            print("\n" + result)
            plaintext_byte = 16 ^ get_byte(cipher_text, len(cipher_text) // 32 - 2, 15) ^ get_byte(cipher_text, 8, 15)
            break

        attempt += 1
        if attempt > 256:
            print("Attempt limit reached, resetting after a 2 second pause...")
            time.sleep(2)
            print("Attempting to reset the socket...")
            close_connection()
            print("Waiting 2 seconds before opening a new socket...")
            time.sleep(2)
            start_connection()
            print("Waiting 1 second before sending data...")
            time.sleep(1)
            return None

    return plaintext_byte


def generate_reports(i):
    """
    Generates the required report and added parameters, given the target i value.
    """
    report = '0' * (51-i)
    added = '0' * (16 - ((51 + 2 - i) % 16))
    if DEBUG:
        print("Generated report", report)
        print("Added", added)
    return report, added


def get_block(cipher_text, i):
    """
    Gets the ith block in the given cipher text.
    Uses zero-indexing.
    """
    return cipher_text[i*32:(i+1)*32]


def get_byte(cipher_text, block, byte):
    """
    Gets the specified byte of the specified block (as an integer).
    Uses zero-indexing.
    """
    return int(get_block(cipher_text, block)[byte*2:(byte+1)*2], 16)


def query_encrypt(report, added):
    if DEBUG_LOW:
        print("Encrypting with report", report)
        print("Added", added)
    while True:
        try:
            send_data(b"e\n" + report.encode("utf-8") + b'\n' + added.encode("utf-8") + b'\n')
            out = get_cipher()
            if DEBUG_LOW:
                print("Returned cipher: " + out)
            break
        except Exception as e:
            print(e)
            print("query_encrypt")
            close_connection()
            start_connection()
    return out


def query_decrypt(cipher):
    if DEBUG_LOW:
        print("Decrypting with cipher", cipher)
    while True:
        try:
            send_data(b"s\n" + cipher.encode("utf-8") + b'\n')
            out = get_decrypt_response()
            if DEBUG_LOW:
                print("Returned response: " + out)
            break
        except Exception as e:
            print(e)
            print("query_decrypt")
            close_connection()
            start_connection()
    return out


def start_connection():
    global s
    if DEBUG:
        print("Starting connection...")
    while True:
        try:
            s = socket.socket()
            s.settimeout(3)
            s.connect((SERVER, PORT))
            get_prompt()
            break
        except Exception as e:
            print(e)
            print("start_connection")


def close_connection():
    global s
    if DEBUG:
        print("Closing connection...")
    try:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except Exception as e:
        print(e)
        print("close_connection")
        s = socket.socket()


def send_data(data):
    if DEBUG_LOW:
        print("Sending data " + data.decode("utf-8"), end='')
    s.sendall(data)


def get_prompt():
    _ = s.recv(BUFFER_SIZE)
    _ = s.recv(BUFFER_SIZE)


def get_cipher():
    _ = s.recv(BUFFER_SIZE)
    cipher = s.recv(BUFFER_SIZE).decode("utf-8")
    cipher = cipher[cipher.find("encrypted: ") + 11:cipher.find("Select an option:")]
    return cipher


def get_decrypt_response():
    _ = s.recv(BUFFER_SIZE)
    response = s.recv(BUFFER_SIZE).decode("utf-8")
    response = response[:response.find("Select an option:")]
    return response


if __name__ == "__main__":
    main()
