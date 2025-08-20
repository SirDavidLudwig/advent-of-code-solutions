from aoc import *

inp = sys.stdin.read().rstrip()

values = []
for line in inp.split("\n"):
    values.append(ints(line))

safe = 0
for row in values:
    i = row[0]
    is_safe = True
    sign = np.sign(row[1] - row[0])
    for j in row[1:]:
        if np.sign(j - i) != sign:
            is_safe = False
            break
        if abs(i-j) < 1 or abs(i-j) > 3:
            is_safe = False
            break
        i = j
    safe += is_safe
print(safe)
