s1, s2 = input().split()
fout = "."*len(s1)
index1 = 0
index2 = 0
for i in range(len(s1)):
    if s1[i] in s2:
        index2 = s2.index(s1[i])
        break

index1 = i

for j in range(len(s2)):
    if j == index2:
        print(s1)
    else:
        out = fout[:index1] + s2[j] + fout[index1+1:]
        print(out)
        
