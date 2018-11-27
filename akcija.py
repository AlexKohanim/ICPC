import bisect
tot = 0
n = int(input())
books = sorted([int(input()) for _ in range(n)]) # 0.20 secs
#for _ in range(n):
#    bisect.insort(books, int(input())) # > 1.0 secs

offset = n % 3
for i in range(offset):
    tot += books[0]
    del books[0]
for i in range(n -1 , 0, -3):
    tot += books[i]
    tot += books[i-1]
    
print(tot)
