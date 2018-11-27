for _ in range(int(input())):
    num = input()[::-1]
    for i in range(len(num)):
        if num[i] != '0':
            if i == 0:
                num = str(int(num[i])-1) + num[i+1:]
            else:
                num = num[:i] + str(int(num[i])-1) + num[i+1:]
            print(int(num[::-1]))
            break
            
            
