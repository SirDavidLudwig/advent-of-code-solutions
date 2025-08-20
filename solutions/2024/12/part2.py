from aoc import *

grid = arr([list(line.rstrip()) for line in sys.stdin.readlines()])
fences = np.full_like(grid, 0, dtype=np.int64)

deltas = arr([
    [-1, 0], # 1
    [1, 0],  # 2
    [0, -1], # 4
    [0, 1]   # 8
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
        for k, delta in enumerate(deltas):
            flag = 1 << k
            npos = [i, j] + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                fences[(i, j)] |= flag
                continue
            if grid[*npos] == c:
                continue
            fences[(i, j)] |= flag

processed = set()
regions = []
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (i, j) in processed:
            continue
        region = extract_region(i, j)
        processed.update(set(region))
        regions.append(region)

def find_connected_fence(i, j, mask):
    c = grid[i, j]
    connected = []
    q = []
    if (fences[i, j] & mask) > 0:
        q.append((i, j))
    seen = set()
    while len(q) > 0:
        i, j = q.pop()
        if (i, j) in seen:
            continue
        connected.append((i, j))
        seen.add((i, j))
        for delta in deltas:
            (ni, nj) = npos = [i, j] + delta
            if np.any(npos < 0) or np.any(npos >= grid.shape):
                continue
            if grid[*npos] != c:
                continue
            if fences[*npos] & mask == 0:
                continue
            if (ni, nj) in seen:
                continue
            q.append((ni, nj))
    return connected


processed = set()
ans = 0
for region in regions:
    sides = 0
    for pos in region:
        for k in range(4):
            fence_mask = 1 << k
            if (pos, fence_mask) in processed:
                continue
            connected = find_connected_fence(*pos, fence_mask)
            for p in connected:
                processed.add((p, fence_mask))
            sides += len(connected) > 0
    ans += sides*len(region)
print(ans)
