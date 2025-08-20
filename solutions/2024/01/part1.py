from aoc import *

x = np.sort(arr(map(ints, rlines(sys.stdin.read()))).T, 1)

print(np.sum(np.abs(x[0] - x[1])))
