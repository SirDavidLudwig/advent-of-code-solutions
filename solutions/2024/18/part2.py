from aoc import *

n, m = 70, 70

data = [tuple(ints(line.strip())[::-1]) for line in sys.stdin]
data = data

def neighbors(state, datamap):
    i, j = state
    for d in dir:
        di, dj = dir.delta(d)
        ni = i+di
        nj = j+dj
        if ni not in range(0, n+1) or nj not in range(0, m+1):
            continue
        if (ni, nj) in datamap:
            continue
        yield (ni, nj)

def find_goal(start, datamap):
    q = set([start])
    seen = set()
    while len(q) > 0:
        i, j = q.pop()
        if i == 70 and j == 70:
            return True
        seen.add((i, j))
        for nstate in neighbors((i, j), datamap):
            if nstate in datamap:
                continue
            if nstate in seen or nstate in q:
                continue
            q.add(nstate)
    return False

import time
t = time.time()

# for m in range(1, len(data)):
#     datamap = set(data[:0])
#     found = find_goal((0, 0), datamap)
#     print(found)
#     if not found:
#         break


left = 0
right = len(data)
while left < right:
    m = (right + left) // 2
    datamap = set(data[:m])
    found = find_goal((0, 0), datamap)
    if found:
        left = m + 1
    else:
        right = m

y, x = data[m]
print(time.time() - t)
print(f"{x},{y}")