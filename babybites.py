input()
l = input().split()
l.insert(0,'0')
for num in range(len(l)):
    if not (not l[num].isdigit() or int(l[num]) == num):
        print("something is fishy")
        break
else:
    print("makes sense")
    
