from aoc import *
from itertools import combinations_with_replacement

grid = np.array([list(line.strip()) for line in sys.stdin])
agrid = grid.copy()

freqs = set(np.unique(grid))
freqs.remove('.')

for f in freqs:
    positions = np.argwhere(grid == f)
    for a, b in combinations(positions, 2):
        d = b - a
        na = a - d
        nb = b + d
        while np.all(na >= 0) and np.all(na < grid.shape):
            agrid[*na] = '#'
            na -= d
        while np.all(nb >= 0) and np.all(nb < grid.shape):
            agrid[*nb] = '#'
            nb += d

ans = len(np.argwhere(agrid != '.'))

for row in agrid:
    print("".join(row))

print(ans)
