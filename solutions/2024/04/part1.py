from aoc import *

inp = sys.stdin.read().rstrip()

grid = inp.split('\n')

ans = 0

def check(i, j):
    total = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            try:
                total += all(
                    0 <= i+di*x and 0 <= j+dj*x and grid[i+di*x][j+dj*x] == c
                    for x, c in enumerate("XMAS")
                )
            except IndexError:
                continue

    return total

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "X":
            continue
        ans += check(i, j)

print(ans)
