from aoc import *
import numpy as np
from pqdict import pqdict
import sys

grid = np.array([list(line.rstrip()) for line in sys.stdin])
distance_map = np.full(grid.shape, np.inf, dtype=float)
n, m = grid.shape

start = tuple(np.argwhere(grid == 'S')[0])
end = tuple(np.argwhere(grid == 'E')[0])

q = [(0, end)]
while len(q) > 0:
    cost, state = q.pop(0)
    distance_map[*state] = cost
    ncost = cost + 1
    for d in dir:
        di, dj = dir.delta(d)
        ni, nj = state[0] + di, state[1] + dj
        if grid[ni, nj] == '#':
            continue
        if ncost >= distance_map[ni, nj]:
            continue
        distance_map[ni, nj] = ncost
        q.append((ncost, (ni, nj)))

def neighbors(state):
    (i, j), cheat_positions = state
    for d in dir:
        di, dj = dir.delta(d)
        ni = i+di
        nj = j+dj
        cheat_active = len(cheat_positions) > 0
        if ni in (0, n-1) or nj in (0, m-1):
            continue
        if grid[ni, nj] =='#':
            if len(cheat_positions) >= 2:
                continue
            cheat_active = True
        ncheat = cheat_positions
        if cheat_active and len(cheat_positions) == 0:
            ncheat = ((i, j)),
        if cheat_active and len(cheat_positions) < 2:
            ncheat = ncheat + ((ni, nj),)
        yield 1, ((ni, nj), ncheat)

# def construct_cheat_deltas(n):
#     q = [(0, (0, 0))]
#     visited = set()
#     while len(q) > 0:
#         cost, (i, j) = q.pop(0)
#         visited.add((i, j))
#         for d in dir:
#             delta = dir.delta(d)
#             nstate = tuple(delta + (i, j))
#             if nstate in visited:
#                 continue
#             if cost + 1 > n:
#                 continue
#             q.append((cost + 1, nstate))
#     return visited - set((0, 0))
# cheat_deltas = construct_cheat_deltas(2)

# def neighbors(state):
#     (i, j), cheat = state
#     for d in dir:
#         di, dj in dir.delta(d)
#         ni = i+di
#         nj = j+dj
#         if ni in (0, n-1) or nj in (0, m-1):
#             continue
#         if grid[ni, nj] == '#':
#             if cheat is None:
#                 for delta in cheat_deltas
#             cheat_active = True
#         ncheat = cheat_positions
#         if cheat_active and len(cheat_positions) == 0:
#             ncheat = ((i, j)),
#         if cheat_active and len(cheat_positions) < 2:
#             ncheat = ncheat + ((ni, nj),)
#         yield 1, ((ni, nj), ncheat)

def search2(initial_state):
    q = pqdict.minpq()
    q[initial_state] = 0
    visited = set()
    while len(q) > 0:
        state, cost = q.popitem()
        if state in visited:
            continue
        visited.add(state)
        if len(state[1]) > 0 and state[0] != end and not np.isinf(distance_map[*state[0]]):
            ncost = cost + distance_map[*state[0]]
            if ncost < 84:
                q[(end, state[1])] = ncost
                print((state[0], state[1]), ncost, cost, distance_map[*state[0]])
            continue
        if state[0] == end:
            yield cost
        for ncost, neighbor in neighbors(state):
            if neighbor in visited:
                continue
            q[neighbor] = (cost + ncost)

# benchmark: 9416
benchmark = 84

# benchmark = 9416 - 100

# # benchmark = min(search(initial_state, neighbors=neighbors, heuristic=heuristic, goal=lambda node: np.all(node.state[0] == end))).cost

# # print(list(neighbors(state)))


from tqdm import tqdm

counts = Counter()
initial_state = (start, tuple())
for cost in tqdm(search2(initial_state)):
    if cost >= benchmark:
        break
    counts[benchmark - cost] += 1
print(dict(sorted(counts.items())))
print(sum(counts.values()))
print("Done")


print(distance_map)