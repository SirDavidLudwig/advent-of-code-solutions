# from aoc import *

# grid = arr([[c for c in line.strip()] for line in sys.stdin])

# kernel = arr([
#     ["M", " ", "M"],
#     [" ", "A", " "],
#     ["S", " ", "S"],
# ])
# mask = kernel == " "

# ans = 0
# for _ in range(4):
#     np.rot90(grid)
#     for i in range(grid.shape[0] - 3):
#         for j in range(grid.shape[1] - 3):
#             ans += np.all(np.logical_or(mask, kernel == grid[i:i+3,j:j+3]))
# print(ans)


from aoc import *

inp = sys.stdin.read().rstrip()
# print(inp)

grid = inp.split('\n')

ans = 0

def check(i, j):
    if i <= 0 or j <=0 or i >= len(grid) - 1 or j >= len(grid[0]) - 1:
        return 0
    found = 0
    for di, dj in [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1)
    ]:
        found += grid[i-di][j-dj] == 'M' and grid[i+di][j+dj] == "S"
    return found == 2

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "A":
            continue
        ans += check(i, j)

print(ans)
