test_cases = int(input())
for _ in range(test_cases):
    m, l = map(int, input().split())
    vals = [0]*l
    for __ in range(m):
        cur = input()
        for i in range(len(cur)):
            if int(cur[i]) == 1:
                vals[i] += 1
            else:
                vals[i] -= 1
    for v in vals:
        print(1 if v > 0 else 0, end = "")
    print()
