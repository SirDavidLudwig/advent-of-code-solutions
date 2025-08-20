from aoc import *

inp = sys.stdin.read().rstrip()

grid, moves = inp.split('\n\n')
grid = grid.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
grid = arr([list(r) for r in grid.rstrip().split('\n')])

moves = moves.rstrip().replace('\n', '').replace('<', 'w') \
    .replace('>', 'e') \
    .replace('v', 's') \
    .replace('^', 'n')

pos = np.argwhere(grid == '@')[0]

def try_push_horizontal(pos, delta):
    npos = pos + delta
    if grid[*npos] == '#':
        return False
    if grid[*npos] == '.' or try_push(npos, delta):
        grid[*npos] = grid[*pos]
        grid[*pos] = '.'
        return True
    return False

def try_push(pos, delta):
    if delta[0] == 0:
        return try_push_horizontal(pos, delta)
    q = [pos]
    to_push = set()
    while len(q) > 0:
        p = q.pop(0)
        to_push.add(farr(p))
        npos = p + delta
        if grid[*npos] == '#':
            return False
        if grid[*npos] in '[]':
            q.append(npos)
            if grid[*npos] == '[':
                q.append(npos + [0, 1])
            else:
                q.append(npos + [0, -1])
    to_push = sorted(to_push, key=lambda x: -delta[0]*x[0])
    for p in to_push:
        npos = p + delta
        grid[*npos] = grid[*p]
        grid[*p] = '.'
    return True

for move in moves:
    delta = dir.delta(move)
    if try_push(pos, delta):
        pos += delta
ans = 0
for box in np.argwhere(grid == '['):
    ans += 100*box[0] + box[1]

print(ans)
