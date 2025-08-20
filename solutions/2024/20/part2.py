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

for node in search(tuple(end), neighbors):
    distance_map[*node.state] = node.cost

diamond = set(dir.delta_diamond(20))

def try_cheat(pos):
    results = []
    for delta in diamond:
        npos = arr(delta) + pos
        d = np.linalg.norm(npos - pos, ord=1)
        if not within(npos, -1, grid.shape, inclusive=False):
            continue
        if distance_map[*npos] + d >= distance_map[*pos]:
            continue
        results.append(int(distance_map[*pos] - distance_map[*npos] - d))
    return results

counts = Counter()
from tqdm import tqdm
for state in tqdm(np.argwhere(~np.isinf(distance_map))):
    for c in try_cheat(state):
        counts[c] += 1

# print(dict(x for x in sorted(counts.items()) if x[0] >= 100))
print(sum(v for c, v in counts.items() if c >= 100))

#           979012
# too high: 1023644