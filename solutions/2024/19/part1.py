from aoc import *
from functools import cache

inp = sys.stdin.read().rstrip()

patterns, inp = inp.split('\n\n')
patterns = set(patterns.split(', '))

longest = max(map(len, patterns))

@cache
def is_possible(pattern):
    if len(pattern) == 0 or pattern in patterns:
        return True
    for i in range(1, longest + 1):
        if pattern[:i] not in patterns:
            continue
        if is_possible(pattern[i:]):
            return True
    return False

from tqdm import tqdm

ans = 0
for line in inp.split('\n'):
    ans += is_possible(line)
    print(line)
    print(ans)

# print(inp)


print(ans)
print("Done")