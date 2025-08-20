from aoc import *

grid = arr([list(r.rstrip()) for r in sys.stdin])

start = tuple(np.argwhere(grid == 'S')[0])
end = tuple(np.argwhere(grid == 'E')[0])

def neighbors(node):
    p, d = node.state
    dirs = [
        (0, d),
        (1000, dir.turn(d, 90)),
        (1000, dir.turn(d, -90))
    ]
    for turn_cost, nd in dirs:
        delta = dir.delta(nd)
        npos = p + delta
        if grid[*npos] == '#':
            continue
        yield turn_cost + 1, (tuple(npos), nd)

def heuristic(node):
    return np.linalg.norm(arr(end) - node.state[0])

initial_state = (start, 'e')

node = next(search(initial_state, neighbors, heuristic=heuristic, goal=lambda node: np.all(node.state[0] == end)))
print(node.cost)
