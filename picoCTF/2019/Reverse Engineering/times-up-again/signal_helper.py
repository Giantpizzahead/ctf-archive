from subprocess import *
from time import sleep
import signal

LOCATION = "/problems/time-s-up--again-_3_f7219b295d1ce306013aea2d0ab82c27"
PROG_NAME = "times-up-again"
SLEEP_TIME = 0.0001

p = Popen([LOCATION + PROG_NAME], cwd=LOCATION, stdin=PIPE, stderr=PIPE)

sleep(SLEEP_TIME)

# With any luck, the process will be stopped right before it sets the alarm...
# but after it's printed the problem! If that happens, we have infinite time
# to solve it.
p.send_signal(signal.SIGTSTP)

result = raw_input()

p.send_signal(signal.SIGCONT)
print(p.communicate(result))

# Flag: picoCTF{Hasten. Hurry. Ferrociously Speedy. #1dc758f2}
