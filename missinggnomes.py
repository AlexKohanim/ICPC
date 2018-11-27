n, m = map(int, input().split())
lst = [int(input()) for _ in range(m)]

j = 0

for i in range(1,n+1):
    if i in lst:
        continue
    while j < len(lst) and lst[j] < i:
        print(lst[j])
        j += 1
    print(i)

for x in range(j,len(lst)):
print(lst[x])
