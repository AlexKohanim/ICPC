#!/usr/bin/env python3
import math
x0, y0, x1, y1, x2, y2 = map(int, input().split())

# 4 edges

result = 0.0

if x0 > x1 and x0 < x2 and y0 > y2:
    result = y0 - y2
elif x0 > x2 and y0 > y2:
    result = math.sqrt((x0 - x2)**2 + (y0 - y2)**2)
elif x0 > x2 and y0 > y1 and y0 < y2:
    result = x0 - x2
elif x0 > x2 and y0 < y1:
    result = math.sqrt((x0 - x2)**2 + (y1 - y0)**2)
elif x0 > x1 and x0 < x2 and y0 < y1:
    result = y1 - y0
elif x0 < x1 and y0 < y1:
    result = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
elif x0 < x1 and y0 > y1 and y0 < y2:
    result = x1 - x0
elif x0 < x1 and y0 > y2:
    result = math.sqrt((x1 - x0)**2 + (y0 - y2)**2)
print(result)