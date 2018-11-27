n = int(input())
for _ in range(n):
    i, counter = 1, 1
    move = int(input())
    lst = list(range(1,move + 1))
    lst2 = []
    for i in range(move -1, -1, -1):
        lst2.insert(0, lst[i])
        for j in range(move):
            lst2.insert(0, lst2[-1])
            del lst2[-1]
        move -= 1
    print(" ".join(str(num) for num in lst2))
        
