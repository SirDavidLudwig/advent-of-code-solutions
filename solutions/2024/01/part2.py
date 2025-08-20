from aoc import *

a, b = arr(map(ints, rlines(sys.stdin.read()))).T

counts = Counter(b)
print(sum(x*counts[x] for x in a))
