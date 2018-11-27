from sys import stdin
for line in stdin:
    line = line.strip()
    if len(line) == 0:
        break
    a, b = map(int, line.split())
    print(abs(a - b))
