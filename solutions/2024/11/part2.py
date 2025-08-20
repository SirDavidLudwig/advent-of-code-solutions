from aoc import *
from tqdm import tqdm

values = Counter(ints(sys.stdin.read()))

for _ in tqdm(range(75)):
    current = Counter()
    for x, count in values.items():
        if x == 0:
            current[1] += count
        elif len(str(x)) % 2 == 0:
            y = str(x)
            current[int(y[:len(y)//2])] += count
            current[int(y[len(y)//2:])] += count
        else:
            current[x*2024] += count
    values = current.copy()


print(sum(values.values()))
