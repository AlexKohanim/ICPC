import math
from sys import stdin
for line in stdin:
    line.strip()
    a, b, c = map(int, line.split())
    if a == b == c == 0:
        break
    A = math.acos((-a**2 + b**2 + c**2) / (2*b*c))
    B = math.acos((a**2 - b**2 + c**2) / (2*a*c))
    C = math.acos((a**2 + b**2 - c**2) / (2*a*b))
    print("right" if max(A,B,C) == (3.141592653589793238462643)/2 else "wrong")
