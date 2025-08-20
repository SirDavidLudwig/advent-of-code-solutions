from aoc import *

ans = 0

inp = sys.stdin.read().rstrip()

keypad_grid = [
    '789',
    '456',
    '123',
    ' 0A'
]

directional_grid = [
    ' nA',
    'wse'
]

def build_sequence_map(grid):
    sequence_map = {}
    for si in range(len(grid)):
        for sj in range(len(grid[0])):
            if grid[si][sj] == " ":
                continue
            q = [(si, sj, "")]
            seen = set()
            while len(q) > 0:
                i, j, seq = q.pop(0)
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                a = grid[si][sj]
                b = grid[i][j]
                sequence_map[(a, b)] = seq
                for d in dir:
                    delta = dir.delta(d)
                    ni = i + delta[0]
                    nj = j + delta[1]
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                        continue
                    if grid[ni][nj] == ' ':
                        continue
                    nseq = seq + d
                    q.append((ni, nj, nseq))
    return sequence_map

keypad_sequence_map = build_sequence_map(keypad_grid)
dpad_sequence_map = build_sequence_map(directional_grid)

def activate(state):
    state, seq = state
    i, j = state[0]
    if len(state) == 1:
        return state, seq + keypad_grid[i][j]
    button = directional_grid[i][j]
    if button == "A":
        nstate, result = activate((state[1:], seq))
        return (state[0], *nstate), result
    nstate = move((state[1:], seq), button)
    if nstate is None:
        return (state, seq)
    return ((state[0], *nstate[0]), nstate[1])

def move(state, d):
    state, seq = state
    grid = directional_grid if len(state) > 1 else keypad_grid
    i, j = state[0]
    di, dj = dir.delta(d)
    ni, nj = int(i+di), int(j+dj)
    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
        return None
    if grid[ni][nj] == ' ':
        return None
    return (((ni, nj), *state[1:]), seq)

def neighbors(state):
    for d in [*dir, "A"]:
        if d == 'A':
            yield activate(state)
        else:
            nstate = move(state, d)
            if nstate is None:
                continue
            yield nstate

for code in inp.split('\n'):
    initial_state = (((0, 2), (0, 2), (3, 2)), "")
    q = pqdict.minpq()
    q[initial_state] = 0
    visited = set()
    while len(q) > 0:
        state, cost = q.popitem()
        if state in visited:
            continue
        visited.add(state)
        if state[1] == code:
            break
        for neighbor, seq in neighbors(state):
            if not code.startswith(seq):
                continue
            q[(neighbor, seq)] = cost + 1
    ans += cost*ints(code)[0]

print(ans)
# 