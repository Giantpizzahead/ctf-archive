"""
Gets the flag for the "script me" picoCTF challenge when run.
"""

import socket

SERVER = "2018shell.picoctf.com"
PORT = 61344
BUFFER_SIZE = 1024
DEBUG = True
DEBUG_LOW = False
s = socket.socket()


def main():
    start_connection()
    problem_number = 0
    while True:
        problem_number += 1
        sout = receive_data()

        # Check for special outputs
        if sout.find("not correct") != -1:
            # Incorrect answer given
            print(sout)
            close_connection()
            exit(1)
        elif sout.find('}') != -1:
            # Flag found
            print(sout)
            close_connection()
            exit()

        problem = get_problem(sout)
        if DEBUG_LOW:
            print(sout)
        elif DEBUG:
            print("\nProblem #" + str(problem_number))
            print(problem + " = ?")

        '''
        # Interactive solving
        
        sin = input("> ").encode("utf-8")
        send_data(sin + b"\n")
        '''

        # Automatic solving
        answer = solve_problem(problem)
        if DEBUG:
            print("Answer: " + answer)
        answer = answer.encode("utf-8")
        send_data(answer + b"\n")


def solve_problem(problem):
    problem_list = problem.split(" + ")
    if DEBUG:
        problem_info(problem_list)
    if DEBUG_LOW:
        print(problem_list)

    # Generate initial counts for each term
    counts = initial_counts(problem_list)

    # Combine each term from left to right
    curr_answer = problem_list[0]
    curr_counts = counts[0]
    for i in range(1, len(problem_list)):
        curr_answer = combine_terms(curr_answer, problem_list[i], curr_counts, counts[i])
        curr_counts = find_counts(curr_answer)
        if DEBUG_LOW:
            print("After combining term " + str(i+1) + ", answer is " + curr_answer)

    # Return the answer
    return curr_answer


def combine_terms(t1, t2, t1_counts, t2_counts):
    # combine rule
    if t1_counts[0] == t2_counts[0]:
        return t1 + t2

    # absorb-right / combined-absorb-right / absorb-combined-right rules
    if t1_counts[0] > t2_counts[0]: # and not t2_counts[1]:
        return t1[:-1] + t2 + t1[-1]

    # absorb-left / combined-absorb-left / absorb-combined-left rules
    if t1_counts[0] < t2_counts[0]: # and not t1_counts[1]:
        return t2[0] + t1 + t2[1:]

    '''
    # absorb-combined-left rule
    # No need to check if separated since if the program got this far, none of the other rules applied
    if t1_counts[0] > t2_counts[0]:
        return t1[0] + t2 + t1[1:]

    # absorb-combined-right rule
    if t2_counts[0] > t1_counts[0]:
        return t2[:-1] + t1 + t2[-1]
    '''

    # Raise an exception if none of the rules applied
    raise("Error combining terms {} and {} with counts {} and {}".format(t1, t2, t1_counts, t2_counts))


def initial_counts(problem_list):
    counts = []

    # For each term, find the max # of parentheses it opens to, and see if it's separated
    for term in problem_list:
        curr_counts = find_counts(term)

        # Record results
        counts.append(curr_counts)
        if DEBUG_LOW:
            print("Max = {}, Sep = {} -> {}".format(curr_counts[0], curr_counts[1], term))

    return counts


def find_counts(term):
    max_parens = 0
    curr_parens = 0
    is_separated = False
    for c in term:
        if c == '(':
            curr_parens += 1
        elif c == ')':
            curr_parens -= 1

        max_parens = max(curr_parens, max_parens)
        if curr_parens == 0:
            # Record that it's been completely enclosed
            curr_parens = -999
        elif curr_parens == -998:
            # This term is separated, no need to check further
            is_separated = True
            break

    # Return results
    return max_parens, is_separated


def problem_info(problem_list):
    print("# of terms: " + str(len(problem_list)))
    print("# of parentheses: " + str(sum([len(x) for x in problem_list])))


def get_problem(data):
    problem_end = data.find(" = ???")
    problem = ""
    i = problem_end - 1
    while data[i] != '\n':
        problem += data[i]
        i -= 1
    return problem[::-1]


def start_connection():
    if DEBUG:
        print("Starting connection...")
    s.connect((SERVER, PORT))


def close_connection():
    if DEBUG:
        print("Closing connection...")
    s.close()


def send_data(data):
    s.sendall(data)


def receive_data():
    out = b''
    line = s.recv(BUFFER_SIZE)

    # Get all the output lines
    while True:
        out += line

        # Check for flag found, at end of output, or incorrect answer
        if line.find(b'>') != -1 or line.find(b'}') != -1:
            break

        line = s.recv(BUFFER_SIZE)

    return out.decode("utf-8")


if __name__ == "__main__":
    main()
