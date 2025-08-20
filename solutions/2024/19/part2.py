from aoc import *
from functools import cache

inp = sys.stdin.read().rstrip()

pattern_pieces, inp = inp.split('\n\n')
pattern_pieces = set(pattern_pieces.split(', '))

longest = max(map(len, pattern_pieces))

@cache
def is_possible(pattern):
    if len(pattern) == 0:
        return 1
    total = 0
    for i in range(1, min(longest + 1, len(pattern)+1)):
        if pattern[:i] not in pattern_pieces:
            continue
        if c := is_possible(pattern[i:]):
            total += c
    return total

from tqdm import tqdm

# print(is_possible("rrbgbr"))

ans = 0
for line in inp.split('\n'):
    c = is_possible(line)
    print(line, c)
    ans += c


print(ans)