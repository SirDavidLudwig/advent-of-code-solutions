from aoc import *

inp = sys.stdin.read().rstrip()

ans = 0

la, lb = inp.split('\n\n')

la = [ints(x) for x in la.split('\n')]
lb = [ints(x) for x in lb.split('\n')]

order = {}
for a, b in la:
    if a not in order:
        order[a] = set()
    order[a].add(b)

def is_valid_order(l):
    for i, x in enumerate(l):
        if x not in order:
            continue
        for y in order[x]:
            if y in l and l.index(y) < i:
                return False
    return True

for l in lb:
    if is_valid_order(l):
        ans += l[len(l)//2]
print(ans)
