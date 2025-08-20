from aoc import *
from functools import cache

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

sign_to_vd = {-1: 'n', 0: '', 1: 's'}
sign_to_hd = {-1: 'w', 0: '', 1: 'e'}

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def build_sequence_map(grid):
    sequence_map = {}
    for si in range(len(grid)):
        for sj in range(len(grid[0])):
            a = grid[si][sj]
            if a == ' ':
                continue
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    b = grid[i][j]
                    if b == ' ':
                        continue
                    di, dj = i-si, j-sj
                    v = sign_to_vd[sign(di)]*abs(di)
                    h = sign_to_hd[sign(dj)]*abs(dj)
                    sequence_map[(a, b)] = set()

                    # Validate the move sequence
                    for seq in (v+h, h+v):
                        ci, cj = si, sj
                        for d in seq:
                            di, dj = dir.delta(d)
                            ci += di
                            cj += dj
                            if grid[ci][cj] ==' ':
                                break
                        else:
                            sequence_map[(a, b)].add(seq + 'A')
                        
    return sequence_map

keypad_sequence_map = build_sequence_map(keypad_grid)
dpad_sequence_map = build_sequence_map(directional_grid)

@cache
def shortest_path(src, dest, n_dpads, dpad_i=-1):
    if dpad_i >= n_dpads:
        return 1
    sequence_map = dpad_sequence_map
    if dpad_i == -1:
        sequence_map = keypad_sequence_map
    best_cost = np.inf
    possible_paths = sequence_map[(src, dest)]
    for possible_path in possible_paths:
        dpad_state = 'A'
        cost = 0
        for d in possible_path:
            if dpad_state == d:
                cost += 1
            else:
                cost += shortest_path(dpad_state, d, n_dpads, dpad_i+1)
            dpad_state = d
        best_cost = min(best_cost, cost)
    return best_cost

for code in inp.rstrip().split('\n'):
    l = 0
    state = 'A'
    for c in code:
        l += shortest_path(state, c, 25)
        state = c
    ans += l*ints(code)[0]

print(ans)
