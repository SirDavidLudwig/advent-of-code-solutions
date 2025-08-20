from aoc import *


def valid(target, remaining, current=None):
    current = current or 0
    if len(remaining) == 0:
        return current == target
    return valid(target, remaining[1:], current + remaining[0]) \
        or valid(target, remaining[1:], current * remaining[0])

ans = 0
for line in sys.stdin.readlines():
    target, *b = ints(line)
    if valid(target, b):
        ans += target

print(ans)
