from aoc import *

grid = arr([list(l.rstrip()) for l in sys.stdin])
distance_map = np.full(grid.shape, np.inf, dtype=float)

start = np.argwhere(grid == 'S')[0]
end = np.argwhere(grid == 'E')[0]

def neighbors(node):
    state = node.state
    for delta in map(dir.delta, dir):
        nstate = state + delta
        if grid[*nstate] == '#':
            continue
        yield 1, tuple(nstate)

def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

for node in search(tuple(end), neighbors):
    distance_map[*node.state] = node.cost

diamond = set(dir.delta_diamond(20))

def try_cheat(pos):
    results = []
    i, j = pos
    for di, dj in diamond:
        ni = i+di
        nj = j+dj
        d = manhattan(pos, (ni, nj))
        if ni <= 0 or nj <= 0 or ni >= grid.shape[0] - 1 or nj >= grid.shape[1] - 1:
            continue
        if (dn := distance_map[ni, nj]) + d >= distance_map[*pos]:
            continue
        results.append(int(distance_map[*pos] - dn - d))
    return results

counts = Counter()
from tqdm import tqdm
for state in tqdm(np.argwhere(~np.isinf(distance_map))):
    for c in try_cheat(tuple(state)):
        counts[c] += 1

# print(dict(x for x in sorted(counts.items()) if x[0] >= 100))
print(sum(v for c, v in counts.items() if c >= 100))

#           979012
# too high: 1023644