r, s, k = map(int, input().split())
flies = set()
for i in range(r):
    for j, c in enumerate(input()):
        if c == '*':
            flies.add((j, i))

maximize = ((), -1)
for i in range(r - k + 1):
    for j in range(s - k + 1):
        counter = 0
        for x, y in flies:
            if i < y < i + k - 1 and j < x < j + k - 1:
                counter += 1
        if counter > maximize[1]:
            maximize = ((j, i), counter)

print(maximize[1])
es = maximize[0]
d = {
    es: '+',
    (es[0] + k - 1, es[1]): '+',
    (es[0], es[1] + k - 1): '+',
    (es[0] + k - 1, es[1] + k - 1): '+',
}
for i in range(1, k - 1):
    d[(es[0] + i, es[1])] = '-'
    d[(es[0] + i, es[1] + k - 1)] = '-'
for i in range(1, k - 1):
    d[(es[0], es[1] + i)] = '|'
    d[(es[0] + k - 1, es[1] + i)] = '|'

for i in range(r):
    print(''.join([d[(j, i)] if (j, i) in d else ('*' if (j, i) in flies else '.') for j in range(s)]))
