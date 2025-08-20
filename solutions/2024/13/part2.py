from aoc import *
from tqdm import tqdm

inp = sys.stdin.read().rstrip()

ans = 0
for group in rgroups(inp):
    a, b, c = arr(map(ints, group.split('\n')))
    c += 10000000000000
    A = arr([a, b]).T
    presses = np.round(np.linalg.solve(A, c))
    if not np.all(np.dot(A, presses) == c):
        continue
    ans += int(np.dot([3, 1], presses))

print(ans)
