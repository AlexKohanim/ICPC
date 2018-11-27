for _ in range(int(input())):
    line = list(map(int, input().split()))
    n = line.pop(0)
    average = sum(line)/n
    m = sum([1 for e in line if e > average])
    print(format((m/n)*100, '.3f'), end="%\n")
