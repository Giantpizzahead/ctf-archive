

arr_n = []
arr_e = []

with open('publickeys.txt', 'r') as fin:
  while True:
    a = fin.readline()
    b = fin.readline()
    fin.readline()
    if a:
      n = int(a.split()[2], 16)
      e = int(b.split()[2], 16)
      arr_n.append(n)
      arr_e.append(e)
    else:
      break

# Check for gcd