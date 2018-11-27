def toDigits(n, b):
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def fromDigits(digits, b):
    n = 0
    for d in digits:
        n = b * n + d
    return n

def convertBase(digits, b, c):
    return toDigits(fromDigits(digits, b), c)

n = int(input())
for cn in range(n):
    an, sl, tl = input().split()
    num_pos = []
    b = len(sl)
    b2 = len(tl)
    for v in an:
        num_pos.append(sl.index(v))
    num = convertBase(num_pos, b, b2)
    print("Case #" + str(cn+1) + ":", end = " ")
    for nu in num:
        print(tl[nu], end = "")
    print()
    #print(num, num_pos)
