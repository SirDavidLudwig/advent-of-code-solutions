from aoc import *

inp = sys.stdin.read().rstrip()
# print(inp)

grid = np.array([list(map(int, line)) for line in rlines(inp)])

trail_heads = np.argwhere(grid == 0)

deltas = np.array([
    (-1, 0),
    (1, 0),
    (0, -1,),
    (0, 1)
])

def solve(start):
    print(start)
    q = [(start, None)]
    seen = set()
    score = 0
    while len(q) > 0:
        pos, path = q.pop()
        if (*pos, path) in seen:
            continue
        seen.add((*pos, path))
        if grid[*pos] == 9:
            score += 1
            continue
        for delta in deltas:
            npos = pos + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                continue
            if grid[*npos] != grid[*pos] + 1:
                continue
            new_path = (*pos, path)
            if (*npos, new_path) in seen:
                continue
            q.append((npos, new_path))
    return score

ans = 0
for head in trail_heads:
    print(head)
    ans += solve(head)

print(ans)
