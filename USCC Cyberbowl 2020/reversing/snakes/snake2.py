from hashlib import md5
from itertools import cycle
import random

def em_dee_5(huh):
    m = md5()
    m.update(huh)
    return m.hexdigest()


def ex_or(m, k):
    return bytes([i ^ j for i, j in zip(m, cycle(k))])


def meeny():
    return 'biNYNk8LaURGSX0jLU08PA=='


def moe():
    return 'ImpHOjBmdU85VD5mIl9qJQ=='


def miny():
    return 'Zgp9dVdJDGoNTFFFeStbNQ=='


def eeny():
    return 'YG0hLk0icXwLcmZVYF1zVg=='


def get_flag(order):
    fs = [
     meeny, miny, moe, eeny]
    co = [int(x[(-1)]) for x in order]
    final = ''.join([em_dee_5(str.encode(fs[x]())) for x in co])
    return em_dee_5(str.encode(final))[::-1]


if __name__ == '__main__':
    magicz = b'ba&v\x1d\x01SVDkKCUEj\\YjG\nR\\g@_\x06TPP\x01\x07\x17R\x13\x18'
    for wut in range(1000, 100000):
        print(wut)
        random.seed(int(wut))
        yeah = [str(random.randint(1000, 10000)) for x in range(0, 4)]
        try:
            flag = get_flag(yeah)
            flag = ex_or(magicz, str.encode(flag)).decode()
            if 'USCC' in flag:
                print('Here is your flag:', flag)
                input()
            else:
                print('Bag flag')
        except:
            print('Try again :)')
