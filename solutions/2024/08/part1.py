from aoc import *

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
        if np.all(na >= 0) and np.all(na < grid.shape):
            agrid[*na] = '#'
        if np.all(nb >= 0) and np.all(nb < grid.shape):
            agrid[*nb] = '#'

ans = len(np.argwhere(agrid == '#'))
