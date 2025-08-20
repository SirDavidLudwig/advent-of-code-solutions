from aoc import *
from tqdm import tqdm

def valid(target, remaining, current=None):
    if current is None:
        current = remaining[0]
        return valid(target, remaining[1:], current)
    if len(remaining) == 0:
        return current == target
    return valid(target, remaining[1:], current + remaining[0]) \
        or valid(target, remaining[1:], current * remaining[0]) \
        or valid(target, remaining[1:], int(f"{current}{remaining[0]}"))

ans = 0
for line in tqdm(sys.stdin.readlines()):
    target, *b = ints(line)
    if valid(target, b):
        ans += target

print(ans)
