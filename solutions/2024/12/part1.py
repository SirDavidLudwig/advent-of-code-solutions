from aoc import *

grid = arr([list(line.rstrip()) for line in sys.stdin.readlines()])
fences = np.full_like(grid, 4, dtype=np.int64)

deltas = arr([
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
])

def extract_region(i, j):
    c = grid[i, j]
    region = []
    q = [(i, j)]
    seen = set()
    while len(q) > 0:
        i, j = q.pop()
        if (i, j) in seen:
            continue
        region.append((i, j))
        seen.add((i, j))
        for delta in deltas:
            (ni, nj) = npos = [i, j] + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                continue
            if grid[*npos] != c:
                continue
            if (ni, nj) in seen:
                continue
            q.append((ni, nj))
    return region

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        c = grid[i,j]
        for delta in deltas:
            npos = [i, j] + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                continue
            if grid[*npos] != c:
                continue
            fences[i,j] -= 1

processed = set()
regions = []
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (i, j) in processed:
            continue
        region = extract_region(i, j)
        processed.update(set(region))
        regions.append(region)

ans = 0
for region in regions:
    p = 0
    for pos in region:
        p += fences[pos]
    ans += p*len(region)
print(ans)
