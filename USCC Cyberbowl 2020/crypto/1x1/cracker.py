import socket
from time import sleep

s: socket
known_flag = 'U'
flag_length = 64
flag_block_count = 4
# 30 extra padding
# USCC{5l0w_4nd_st34dy_w1n5_7h3_r4c3}

def init_socket():
    global s
    sleep(2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("3.22.198.100", 3202))
    s.recv(4096)
    s.recv(4096)


def query(text):
    s.sendall(bytes(text + '\n', "utf-8"))
    result = b''
    while True:
        part = s.recv(4096)
        result += part
        if len(part) == 0:
            break
    result = result[(result.index(b"ballot.\n") + 8):]
    # print("Query {}".format(text))
    # print(len(result))
    # print(result)
    return result


def split_blocks(chunk):
    blocks = []
    for i in range(len(chunk) // 32):
        blocks.append(chunk[i*32:(i+1)*32])
    return blocks


def get_flag_blocks(query_blocks, num_blocks):
    blocks = []
    print("query blocks length", len(query_blocks))
    for i in range(num_blocks + 1):
        curr_block = b""
        for j in range(i*flag_block_count, (i+1)*flag_block_count):
            curr_block += query_blocks[j]
        blocks.append(curr_block)
    return blocks[:-1], blocks[-1]


def main():
    global known_flag
    while known_flag[-1] != '}':
        try:
            # Figure out next character using a smart technique
            init_socket()
            query_text = 'P' * 2
            # Try every next character
            for i in range(32, 128):
                query_text += 'A' * (flag_length - 1 - len(known_flag)) + known_flag + chr(i)
            # Add final padding for flag block
            query_text += 'A' * (flag_length - 1 - len(known_flag))
            # Query entire thing at once
            query_blocks = split_blocks(query(query_text))[2:]
            query_blocks, flag_block = get_flag_blocks(query_blocks, 96)
            # print("Query blocks", query_blocks)
            # print("Flag block", flag_block)
            # Determine character based on given info
            char_found = False
            for i in range(32, 128):
                if query_blocks[i-32] == flag_block:
                    # Found right character
                    known_flag += chr(i)
                    char_found = True
                    print("Flag character", chr(i))
                    break
            if not char_found:
                print("ERROR; no character found!")
        except Exception as e:
            print("Error occurred; continuing anyway...", e)
    print("FLAG: {}".format(known_flag))


if __name__ == "__main__":
    main()
