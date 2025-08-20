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

keypad_weight_map = {}
dgrid_weight_map = {}

def build_weight_map(grid):
    weights = {}
    for si in range(len(grid)):
        for sj in range(len(grid[0])):
            if grid[si][sj] == " ":
                continue
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == " ":
                        continue
                    weights[(grid[si][sj], grid[i][j])] = abs(i - si) + abs(j - sj)
    return weights

rev_dirs = {
    'n': 's',
    'e': 'w',
    'w': 'e',
    's': 'n'
}

def is_valid_seq(seq):
    if len(seq) <= 2:
        return True
    x = seq[0]
    changed = False
    for c in seq:
        if c != x:
            if changed:
                return False
            x = c
            changed = True
    return seq[0] != rev_dirs[seq[-1]]
    

def build_sequence_map(grid, weight_map):
    sequence_map = {}
    for si in range(len(grid)):
        for sj in range(len(grid[0])):
            a = grid[si][sj]
            if a == " ":
                continue
            q = pqdict.minpq()
            q[(si, sj, "")] = 0
            seen = set()
            while len(q) > 0:
                state, cost = q.popitem()
                i, j, seq = state
                if state in seen:
                    continue
                seen.add(state)
                b = grid[i][j]
                sequence_map[(a, b)] = seq
                for d in dir:
                    delta = dir.delta(d)
                    ni = i + delta[0]
                    nj = j + delta[1]
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
                        continue
                    c = grid[ni][nj]
                    nseq = seq + d
                    if not is_valid_seq(nseq):
                        continue
                    if grid[ni][nj] == ' ':
                        continue
                    q[(ni, nj, nseq)] = cost + 2*weight_map[('A', d)]
    return sequence_map
keypad_weight_map = build_weight_map(keypad_grid)
dpad_weight_map = build_weight_map(directional_grid)

keypad_sequence_map = build_sequence_map(keypad_grid, dpad_weight_map)
dpad_sequence_map = build_sequence_map(directional_grid, dpad_weight_map)
# dpad_sequence_map[('A', 'w')] = 'sww'

for c in keypad_sequence_map.values():
    assert is_valid_seq(c)

# print(keypad_sequence_map)
# print(dpad_sequence_map)

def find_sequence(sequence, grid):
    result = ""
    state = "A"
    for c in sequence:
        result += grid[(state, c)] + 'A'
        state = c
    return result

for code in inp.split('\n'):
    s = find_sequence(code, keypad_sequence_map)
    s = find_sequence(s, dpad_sequence_map)
    # s = find_sequence(s, dpad_sequence_map)
    l = len(s)
    c = int(ints(code)[0])
    print(l, c)

    print(s)

    ans += l*int(ints(code)[0])
    s = find_sequence(s, dpad_sequence_map)

    # sequence = ""
    # for c in code:
    #     sequence += keypad_sequence_map[(keypad_state, c)] + 'A'
    # print(sequence)
    break


# print(ans)
# 