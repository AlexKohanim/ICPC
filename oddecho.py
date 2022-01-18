from sys import stdin
for line_num, line in enumerate(stdin):
    if line_num % 2:
        print(line)