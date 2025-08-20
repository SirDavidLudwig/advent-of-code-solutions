from aoc import *
import operator

inp = sys.stdin.read().rstrip()

inp = inp.split('\n\n')
states = {}
for row in inp[0].split('\n'):
    k, v = row.split(': ')
    states[k] = int(v)

q = []
for row in inp[1].rstrip().split('\n'):
    a, op, b, _, c = row.split()
    q.append((a, op, b, c))

ops = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor
}

while len(q) > 0:
    a, op, b, c = q.pop(0)
    if a not in states or b not in states:
        q.append((a, op, b, c))
        continue
    states[c] = ops[op](states[a], states[b])

ans = 0
result = []
for state, value in states.items():
    if not state.startswith("z"):
        continue
    result.append((int(state[1:]), value))
result.sort(reverse=True)
print(int("".join([str(bit) for _, bit in result]), base=2))

print(ans)
