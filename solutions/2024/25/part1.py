from aoc import *
from itertools import product

inp = sys.stdin.read().rstrip()
locks = []
keys = []

for group in rgroups(inp):
    rows = arr([list(c) for c in group.split('\n')])
    if set(rows[0]) == set('#'):
        locks.append((rows == '#').astype(int))
    else:
        keys.append((rows == '#').astype(int))

ans = 0
for a, b in product(locks, keys):
    ans += not np.any(a + b > 1)

dir(cards=True, diags=True, start="n", direction="clockwise")

print(dir.turn("s", 90))

print(ans)
