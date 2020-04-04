import signal
import os
import threading
import queue
from subprocess import *
from time import sleep

input_queue = queue.Queue()
location = "."
process = Popen([location + "/times-up-again"], cwd=location, stdout=PIPE, stdin=PIPE, stderr=PIPE)
stop_thread = False

def main():
    global stop_thread, process, location, input_queue

    input_thread = "hi"
    i = 1
    amount_to_sleep = 0.001
    while True:
        print("Attempt " + str(i) + " | Sleep amount " + str(amount_to_sleep), end='\r')
        i += 1

        # Create input threaid
        del input_thread
        input_queue = queue.Queue()
        input_thread = threading.Thread(target=add_input)
        input_thread.start()
        process = Popen([location + "/times-up-again"], cwd=location, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        
        sleep(amount_to_sleep)
        process.send_signal(signal.SIGSTOP)
        sleep(0.005)

        # Get output
        stdout = b''
        while not input_queue.empty():
            stdout += input_queue.get()
        
        stdout = stdout.decode('utf-8')

        if not "\n" in stdout:
            # Didn't finish outputting problem
            '''
            print()
            print("Not done " + stdout)
            '''
            amount_to_sleep += 0.00001
            continue
        elif "Setting" in stdout:
            # Didn't finish outputting problem, or paused too late
            '''
            print()
            print("Too much " + stdout)
            '''
            amount_to_sleep -= 0.00001
            continue
        else:
            print("\nSolving...")

        # Solve it
        problem = stdout[0:stdout.index("\n")]
        problem = problem[11:]
        print(problem)
        result = eval(problem)
        print("Answer: ", result)

        print("Now writing answer...")
        answer = str(result).encode('utf-8')
        # process.stdin.write(str(result).encode('utf-8') + b"\n")
        process.send_signal(signal.SIGCONT)
        # print(process.poll())
        print(process.communicate(answer))
        input()


def add_input():
    global stop_thread
    try:
        while not stop_thread:
            input_queue.put(process.stdout.read(1))
    except Exception as e:
        _ = 1
    stop_thread = False

main()
