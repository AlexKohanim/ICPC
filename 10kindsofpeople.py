#!/usr/bin/env python3
r, c = map(int, input().split())
m = []
for _ in range(r):
    m.append(list(input()))
tot = r * c
n_group = 1
group = [0]*tot
    
op = [] # stack
    
for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    sec1 = r1 * c + c1
    sec2 = r2 * c+ c2
    
    if sec1 == sec2:
        print("decimal" if m[r1][c1] == "1" else "binary")
    elif group[sec1] == group[sec2] and group[sec2] == 0:
        # let's do what Austin Showed us
        op.append((r1,c1))
        
        while len(op) > 0:
            cur = op.pop()
            cur_x, cur_y = cur[0], cur[1]
            cur_v = m[cur_x][cur_y]
            secc1 = cur_x * c + cur_y
            if group[secc1] != 0:
                continue
            group[secc1] = n_group
            

            if (cur_x > 0 and m[cur_x-1][cur_y] == cur_v and not group[(cur_x-1)* c + cur_y]):
                op.append((cur_x -1, cur_y))
            if (cur_x < r - 1 and m[cur_x + 1][cur_y] == cur_v and not group[(cur_x + 1) * c+cur_y]):
                op.append((cur_x+1, cur_y))
            if (cur_y > 0 and m[cur_x][cur_y - 1] == cur_v and not group[cur_x * c + cur_y - 1]):
                op.append((cur_x, cur_y - 1))
            if (cur_y < c - 1 and m[cur_x][cur_y + 1] == cur_v and not group[cur_x * c + cur_y + 1]):
                op.append((cur_x, cur_y + 1))

        n_group += 1
        
        if group[sec2] != 0:
            if m[r1][c1] == "1":
                print("decimal")
            else:
                print("binary")
        else:
            print("neither")
        
    elif m[r1][c1] != m[r2][c2]:
        print("neither")
    elif group[sec1] == group[sec2]:
        print("decimal" if m[r1][c1] == "1" else "binary")         
    else:
        print("neither")
