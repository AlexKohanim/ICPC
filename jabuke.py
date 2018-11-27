import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

area = round(abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2), 1)
print(area)

def pointInTriangle(x1, y1, x2, y2, x3, y3, x, y):
    epslon = 0.00005
    a = round(((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3)), 4)
    b = round(((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3)), 4)
    c = 1 - a - b
    return 0 <= a  and a <= 1 + epslon and 0 <= b and b <= 1 + epslon and 0 <= c and c <= 1 + epslon
trees = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    trees += 1 if pointInTriangle(x1, y1, x2, y2, x3, y3, x, y) else 0
print(trees)
