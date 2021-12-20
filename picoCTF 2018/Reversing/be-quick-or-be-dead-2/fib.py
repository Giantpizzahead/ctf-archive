fibs = []

def fib(x):
    fibs.append(0)
    fibs.append(1)
    for i in range(2, x+1):
        fibs.append((fibs[i-1]+fibs[i-2]) % (2147483647 * 2) - 2147483647)
    return fibs[x]

print(fib(48))
