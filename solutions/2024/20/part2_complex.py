from aoc import *

grid = arr([list(l.rstrip()) for l in sys.stdin])
distance_map = np.full(grid.shape, np.inf, dtype=float)

start = np.argwhere(grid == 'S')[0]
end = np.argwhere(grid == 'E')[0]

start = complex(*start)
end = complex(*end)

def neighbors(node):
    state = node.state
    for delta in map(lambda x: complex(*dir.delta(x)), dir):
        nstate = state + delta
        if grid[int(nstate.real), int(nstate.imag)] == '#':
            continue
        yield 1, nstate

def manhattan(a, b):
    c = b - a
    return abs(c.real) + abs(c.imag)

for node in search(end, neighbors):
    distance_map[int(node.state.real), int(node.state.imag)] = node.cost

diamond = set(complex(*delta) for delta in dir.delta_diamond(20))

def try_cheat(pos):
    results = []
    for delta in diamond:
        npos = pos + delta
        d = manhattan(pos, npos)
        if npos.real <= 0 or npos.real <= 0 or npos.imag >= grid.shape[0] - 1 or npos.imag >= grid.shape[1] - 1:
            continue
        if (dn := distance_map[int(npos.real), int(npos.imag)]) + d >= distance_map[int(pos.real), int(pos.imag)]:
            continue
        results.append(int(distance_map[int(pos.real), int(pos.imag)] - dn - d))
    return results

counts = Counter()
from tqdm import tqdm
for state in tqdm(np.argwhere(~np.isinf(distance_map))):
    state = complex(*state)
    for c in try_cheat(state):
        counts[c] += 1

# print(dict(x for x in sorted(counts.items()) if x[0] >= 100))
print(sum(v for c, v in counts.items() if c >= 100))

# #           979012
# # too high: 1023644