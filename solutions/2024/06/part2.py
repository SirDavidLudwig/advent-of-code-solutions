from aoc import *

grid = np.array([list(line.rstrip()) for line in sys.stdin.readlines()])

init_i, init_j = np.argwhere(grid == '^')[0]

deltas = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def run(grid):
    observed = grid.copy()
    d = 0
    i, j = np.argwhere(grid == '^')[0]
    seen = set()
    while (i, j, d) not in seen:
        di, dj = deltas[d]
        ni, nj = i+di, j+dj
        observed[i, j] = 'X'
        if not (0 <= ni < grid.shape[0]) or not (0 <= nj < grid.shape[1]):
            return observed
        if grid[ni, nj] == '#':
            d = (d + 1) % 4
            continue
        seen.add((i, j, d))

        i += di
        j += dj
    return None

observed = run(grid.copy())

ans = 0

from tqdm import tqdm
for oi, oj in tqdm(np.argwhere(observed == 'X')):
    if (oi, oj) == (init_i, init_j):
        continue
    grid[oi,oj] = '#'
    result = run(grid.copy())
    grid[oi,oj] = '.'
    ans += result is None

print(ans)
