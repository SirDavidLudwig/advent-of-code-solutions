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
    q = [start]
    assert np.all(grid[*start] == [0, 0])
    seen = set()
    score = 0
    while len(q) > 0:
        (i, j) = pos = q.pop()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        if grid[*pos] == 9:
            score += 1
            continue
        for delta in deltas:
            npos = pos + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                continue
            if grid[*npos] != grid[*pos] + 1:
                continue
            if (*npos,) in seen:
                continue
            q.append(npos)
    return score


ans = 0
for head in trail_heads:
    ans += solve(head)

print(ans)
