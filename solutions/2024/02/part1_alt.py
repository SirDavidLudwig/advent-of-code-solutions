import numpy as np
import sys

print(sum(
    np.all(np.abs(x) >= 1) and np.all(np.abs(x) <= 3)
    for x in [np.diff(list(map(int, l.split()))) for l in sys.stdin.readlines()]
        if not np.any(x < 0) or np.all(x < 0)
))

