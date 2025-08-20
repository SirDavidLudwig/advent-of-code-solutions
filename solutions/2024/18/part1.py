from aoc import *

n, m = 70, 70

data = [tuple(ints(line.strip())[::-1]) for line in sys.stdin]
data = data[:1024]

datamap = set(data)

def neighbors(node):
    i, j = node.state
    for d in dir:
        di, dj = dir.delta(d)
        ni = i+di
        nj = j+dj
        if ni not in range(0, n+1) or nj not in range(0, m+1):
            continue
        if (ni, nj) in datamap:
            continue
        yield 1, (ni, nj)

def heuristic(node):
    return np.linalg.norm(arr(node.state) - (70, 70))


initial_state = (0, 0)
print(min(search(initial_state, neighbors=neighbors, heuristic=heuristic, goal=lambda node: np.all(node.state == (70, 70)))).cost)