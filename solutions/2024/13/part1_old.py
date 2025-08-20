from aoc import *
from tqdm import tqdm

inp = sys.stdin.read().rstrip()

ans = 0
for group in tqdm(rgroups(inp)):
    a, b, c = map(arr, map(ints, group.split('\n')))

    def neighbors(state):
        for cost, new_state in [(3, tuple(state+a)), (1, tuple(state+b))]:
            if np.any(new_state > c):
                continue
            yield cost, new_state

    costs = [cost for (cost, state, _) in astar((0, 0), neighbors) if np.all(c == state)]
    if len(costs) == 0:
        continue
    ans += min(costs)
print(ans)
