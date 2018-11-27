import math
n = math.log(int(input()), 2)
if int(n) == n:
    print(str(int(n+1)))
else:
    print(str(math.ceil(n)+1))
