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

def build_sequence_map(grid):
    sequence_map = {}
    for si in range(len(grid)):
        for sj in range(len(grid[0])):
            a = grid[si][sj]
            if a == " ":
                continue
            q = [(si, sj, "")]
            seen = set()
            while len(q) > 0:
                i, j, seq = q.pop(0)
                if (i, j) in seen:
                    continue
                seen.add((i, j))
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

keypad_weight_map = build_weight_map(keypad_grid)
dpad_weight_map = build_weight_map(directional_grid)

keypad_sequence_map = build_sequence_map(keypad_grid)
dpad_sequence_map = build_sequence_map(directional_grid)
dpad_sequence_map[('A', 'w')] = 'sww'

for c in keypad_sequence_map.values():
    x = Counter(c)
    letters, counts = map(list, [x.keys(), x.values()])
    if len(letters) == 1:
        continue
    assert c == "".join([l*count for l, count in zip(letters, counts)])

for k, v in keypad_sequence_map.items():
    if v.startswith("n"):
        keypad_sequence_map[k] = v[::-1]

# print(keypad_sequence_map)
# print(dpad_sequence_map)

def find_sequence(sequence, grid):
    result = ""
    state = "A"
    for c in sequence:
        result += grid[(state, c)] + 'A'
        state = c
    return result

print(dpad_sequence_map[('A', 'w')])

# for code in inp.split('\n'):
#     s = code
#     print(s)
#     s = find_sequence(code, keypad_sequence_map)
#     for _ in range(2):
#         s = find_sequence(s, dpad_sequence_map)
#     print("Done")
#     l = len(s)
#     c = int(ints(code)[0])
#     print(l, c)

#     print(s.replace('n', '^').replace('w', '<').replace('e', '>').replace('s', 'v'))
#     print("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")

#     ans += l*int(ints(code)[0])
    # s = find_sequence(s, dpad_sequence_map)

    # sequence = ""
    # for c in code:
    #     sequence += keypad_sequence_map[(keypad_state, c)] + 'A'
    # print(sequence)
    # break


print(ans)
# 