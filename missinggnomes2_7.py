import sys

n, m = sys.stdin.readline().split(" ")
n, m = int(n), int(m)
x = 0
lst = []
st = set()
for i in xrange(m):
    v = int(sys.stdin.readline())
    lst.append(v)
    st.add(v)
    
    
for i in xrange(1, n+1):
    if (i in st): 
        continue
    while (x < len(lst) and lst[x] < i):
        print lst[x]
        x += 1
    print i

while (x < len(lst)):
    print lst[x]
x += 1
