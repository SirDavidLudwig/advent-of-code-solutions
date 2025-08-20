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

inner_diamond = set(dir.delta_diamond(1))
outer_diamond = set(dir.delta_diamond(2)) - inner_diamond

def try_cheat(pos):
    results = []
    for delta in outer_diamond:
        npos = arr(delta) + pos
        if not within(npos, -1, grid.shape, inclusive=False):
            continue
        if distance_map[*npos] + 2 >= distance_map[*pos]:
            continue
        results.append(npos)
    return [int(distance_map[*pos] - distance_map[*npos] - 2) for npos in results]

counts = Counter()
for state in np.argwhere(~np.isinf(distance_map)):
    for c in try_cheat(state):
        counts[c] += 1

print(sum(v for c, v in counts.items() if c >= 100))