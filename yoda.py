#!/usr/bin/env python3

a = list(map(int, list(input())))
b = list(map(int, list(input())))

a_i = len(a) - 1
b_i = len(b) -1

for _ in range(min(len(a),len(b))-1,-1,-1):
    a_value = a[a_i]
    b_value = b[b_i]
    if a_value > b_value:
        del(b[b_i])
    if b_value > a_value:
        del(a[a_i])
    a_i -= 1
    b_i -= 1

print('YODA' if len(a) == 0 else int(''.join(str(x) for x in a)))
print('YODA' if len(b) == 0 else int(''.join(str(x) for x in b)))