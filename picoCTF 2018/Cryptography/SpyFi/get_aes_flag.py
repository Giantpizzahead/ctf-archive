"""
Gets the flag for the "SpyFi" picoCTF challenge when run.
"""

import socket

SERVER = "2018shell.picoctf.com"
PORT = 34490
BUFFER_SIZE = 4096
DEBUG = False
DEBUG_LOW = False
s = socket.socket()


def main():
    known = "picoCTF"
    target_plain = "ode is: picoCTF"
    for i in range(31):
        print("The flag so far: " + known)
        target_cipher = get_target(i)
        blocks = brute_force_ciphers(target_plain)
        if DEBUG:
            print("Target: " + target_cipher)
            print(blocks)
        correct_chr = find_correct_chr(target_cipher, blocks)
        known += correct_chr
        target_plain = target_plain[1:] + correct_chr

    # Print the answer
    print("------------------------------------------------------------")
    print("The flag is:")
    print(known)


def find_correct_chr(target, blocks):
    """
    Finds the correct character when given the target cipher, and the blocks dictionary.
    """
    if target in blocks:
        return blocks[target]
    else:
        return '?'


def brute_force_ciphers(plain):
    """
    Generates all possible cipher blocks from the given plain text, when adding a character to the end.
    Returns a dictionary with format {cipher_block : character_used}.
    """
    # Generate the query
    query = "00000000000"
    min_chr = 32   # Space
    max_chr = 126  # ~
    num_chrs = max_chr - min_chr
    for c in range(min_chr, max_chr + 1):
        curr_query = plain + chr(c)
        query += curr_query

    # Send the query, and get all the blocks
    full_cipher = query_program(query)
    # Generate the dictionary
    blocks = {}
    for i in range(num_chrs + 1):
        blocks[get_block(full_cipher, i + 4)] = chr(min_chr + i)

    return blocks


def get_target(i):
    """
    Gets the target part of the text containing the next character at the end.
    Returns the block cipher at that location.
    """
    # Calculate number of zeroes needed / the target block to look at
    zero_length = 15 - ((i+11) % 16)
    target_block = 5 + ((i+11) // 16)
    report = '0'*zero_length
    full_cipher = query_program(report)

    # Return the correct block
    return get_block(full_cipher, target_block)


def get_block(cipher_text, i):
    """
    Gets the ith block in the given cipher text.
    Uses zero-indexing.
    """
    return cipher_text[i*32:(i+1)*32]


def query_program(report):
    start_connection()
    if DEBUG:
        print("Querying with report " + report)
    send_report(report.encode("utf-8") + b'\n')
    out = get_cipher()
    if DEBUG_LOW:
        print("Returned cipher:\n" + out)
    close_connection()
    return out


def start_connection():
    global s
    if DEBUG_LOW:
        print("Starting connection...")
    s = socket.socket()
    s.connect((SERVER, PORT))
    get_intro()


def close_connection():
    if DEBUG_LOW:
        print("Closing connection...")
    s.close()


def send_report(data):
    if DEBUG_LOW:
        print("Sending data " + data.decode("utf-8"), end='')
    s.sendall(data)


def get_intro():
    _ = s.recv(BUFFER_SIZE)
    _ = s.recv(BUFFER_SIZE)


def get_cipher():
    return s.recv(BUFFER_SIZE).decode("utf-8")


if __name__ == "__main__":
    main()
