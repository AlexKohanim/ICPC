t, k = input().split()
if t == 'E':
    ch = k[0]
    count = 0
    for c in k:
        if not c == ch:
            print(ch,count, end="", sep = "")
            ch = c
            count = 1
        else:
            count += 1
       
    print(ch, count, sep="")
else:
    for i in range(0, len(k), 2):
        print(k[i]*int(k[i+1]), end="")
