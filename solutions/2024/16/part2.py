from aoc import *

grid = arr([list(r.rstrip()) for r in sys.stdin])

start = tuple(np.argwhere(grid == 'S')[0])
end = tuple(np.argwhere(grid == 'E')[0])

def neighbors(state):
    p, d = state
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

def heuristic(state):
    return np.linalg.norm(arr(end) - state[0])

initial_state = (start, 'e')

q = pqdict.minpq()
q[(initial_state, None)] = 0
visited = {} # state: cost, parents
final_states = []
bound = np.inf
while len(q) > 0:
    (state, parent), cost = q.popitem(q)
    if cost > bound:
        break
    if state in visited and cost > visited[state][0]:
        continue
    if state in visited:
        visited[state][1].add(parent)
        continue
    else:
        visited[state] = (cost, set([parent] if parent is not None else []))
    if np.all(state[0] == end):
        bound = cost
        final_states.append(state)
        continue
    for ncost, nstate in neighbors(state):
        if nstate in visited:
            continue
        q[(nstate, state)] = cost + ncost

q = final_states
observed = set()
while len(q) > 0:
    state = q.pop()
    grid[state[0]] = state[1]
    if state not in visited:
        break
    observed.add(state[0])
    q += list(visited[state][1])
print(len(observed))
