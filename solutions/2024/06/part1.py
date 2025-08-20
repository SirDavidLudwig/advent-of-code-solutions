from aoc import *

grid = np.array([list(line.rstrip()) for line in sys.stdin.readlines()])
observed = grid.copy()

deltas = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

d = 0
i, j = np.argwhere(grid == '^')[0]
seen = set()
while (i, j, d) not in seen:
    di, dj = deltas[d]
    ni, nj = i+di, j+dj
    observed[i, j] = 'X'
    if not (0 <= ni < grid.shape[0]) or not (0 <= nj < grid.shape[1]):
        break
    if grid[ni, nj] == '#':
        d = (d + 1) % 4
        continue
    seen.add((i, j, d))
    i += di
    j += dj

print(np.sum(observed == 'X'))

