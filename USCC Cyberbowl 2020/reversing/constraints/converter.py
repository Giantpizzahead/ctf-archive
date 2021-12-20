vars = [44, 62, 41, 40, 88, 51, 104, 69, 116, 49, 36, 43, 60, 92, 116, 85, 92, 63, 34, 92, 35, 75, 106, 87, 33, 114, 45, 49, 102, 68, 121, 77, 36, 97, 56, 60, 100, 118, 35, 70, 77, 93, 106, 96, 41, 36, 90, 62, 85, 119, 99, 94, 54]

with open('reversing/constraints/constraints3.txt', 'r') as fin, open('constraints4.txt', 'w') as fout:
    line = fin.readline()
    for i in range(53):
        print(line.count('vars[{}]'.format(i)))
        line = line.replace('vars[{}]'.format(i), str(vars[i]))
    fout.write(line)
