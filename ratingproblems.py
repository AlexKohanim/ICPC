n, k = map(int, input().split())
total = 0
for _ in range(k):
    total += int(input())
print((total + (-3*(n-k))) / n, (total + 3*(n-k)) / n)
