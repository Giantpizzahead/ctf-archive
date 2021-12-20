nums = map(int, input().strip().split())

START_NUM = 5000

for i in nums:
    print(chr(i-5000), end='')
