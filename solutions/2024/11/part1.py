from aoc import *
from tqdm import tqdm

values = ints(sys.stdin.read())

for _ in tqdm(range(25)):
    current = []
    for x in values:
        if x == 0:
            current.append(1)
        elif len(str(x)) % 2 == 0:
            y = str(x)
            current.append(int(y[:len(y)//2]))
            current.append(int(y[len(y)//2:]))
        else:
            current.append(x*2024)
    values = current


print(len(values))
