from subprocess import *

process = Popen(["/problems/time-s-up_4_548d4bc5ce82bf27864a00001fcbd182/times-up"], cwd="/problems/time-s-up_4_548d4bc5ce82bf27864a00001fcbd182", stdout=PIPE, stdin=PIPE, stderr=PIPE)

problem = process.stdout.readline()
problem = problem[11:]
print(problem)
result = eval(problem)
print("Answer: ", result)
process.stdin.write(str(result) + "\n")
print(process.communicate()[0])
