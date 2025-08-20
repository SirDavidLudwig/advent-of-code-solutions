from aoc import *

inp = sys.stdin.read().rstrip()

values = []
for line in inp.split("\n"):
    values.append(ints(line))

def is_safe(row):
    sign = np.sign(row[1] - row[0])
    for i in range(1, len(row)):
        a, b = row[i-1], row[i]
        if np.sign(b - a) != sign or abs(b-a) < 1 or abs(b-a) > 3:
            return False
    return True

total_safe = 0
for row in values:
    safe = is_safe(row)
    if not safe:
        for i in range(len(row)):
            if safe := is_safe(row[:i] + row[i+1:]):
                break
    total_safe += safe
print(total_safe)
