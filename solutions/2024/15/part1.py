from aoc import *

inp = sys.stdin.read().rstrip()

grid, moves = inp.split('\n\n')
grid = arr([list(r) for r in grid.rstrip().split('\n')])

moves = moves.rstrip().replace('\n', '').replace('<', 'w') \
    .replace('>', 'e') \
    .replace('v', 's') \
    .replace('^', 'n')

ans = 0

pos = np.argwhere(grid == '@')[0]

def try_push(pos, delta):
    npos = pos + delta
    if grid[*npos] == '#':
        return False
    if grid[*npos] == '.' or try_push(npos, delta):
        grid[*npos] = grid[*pos]
        grid[*pos] = '.'
        return True
    return False

for move in moves:
    delta = dir.delta(move)
    if try_push(pos, delta):
        pos += delta
ans = 0
for box in np.argwhere(grid == 'O'):
    ans += 100*box[0] + box[1]

print(ans)
