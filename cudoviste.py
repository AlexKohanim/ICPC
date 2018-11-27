#!/usr/bin/env python3
r, c = map(int, input().split())
results = [0, 0, 0, 0, 0]
grid = [input() for row in range(r)]

#print(grid)

for i in range(r-1):
    for j in range(c-1):
        #print(grid[i+1][j+1])
        # the one liner urge....
        if grid[i][j]  != "#" and grid[i+1][j+1] != "#" and grid[i+1][j] != "#" and grid[i][j+1] != "#":
            #results[(1 if grid[i][j] == "X" else 0) + (1 if grid[i+1][j] == "X" else 0) + (1 if grid[i][j+1] == "X" else 0) + (1 if grid[i+1][j+1] == "X" else 0)] += 1
            n = ((1 if grid[i][j] == "X" else 0) + (1 if grid[i+1][j] == "X" else 0) + (1 if grid[i][j+1] == "X" else 0) + (1 if   grid[i+1][j+1] == "X" else 0))
            #print(results[n])
            results[n] += 1

[print(n) for n in results]
