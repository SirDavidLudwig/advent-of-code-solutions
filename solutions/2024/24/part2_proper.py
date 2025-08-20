from aoc import *
from itertools import product
import operator

ops = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor
}

inp = sys.stdin.read().rstrip()

input_to_output = {}
output_to_input = {}
for row in inp.split('\n\n')[1].rstrip().split('\n'):
    a, op, b, _, c = row.split()
    node = (a, op, b)
    input_to_output[node] = c
    output_to_input[c] = node

def extract(key, states):
    result = 0
    for i in count():
        k = f"{key}{i:02}"
        if k not in states:
            break
        result |= states[k] << i
    return result

def insert(key, value, states):
    states |= {f"{key}{i:02}": int(x) for i, x in enumerate(f"{value:045b}"[::-1])}

def resolve_dependencies(output):
    q = [output]
    dependencies = set()
    while len(q) > 0:
        x = q.pop(0)
        if x not in output_to_input:
            continue
        p = output_to_input[x]
        dependencies.add(p)
        q.append(p[0])
        q.append(p[2])
    output_to_input[output]
    return dependencies

def swap(output_a, output_b):
    gate_a = output_to_input[output_a]
    gate_b = output_to_input[output_b]
    input_to_output[gate_a] = output_b
    input_to_output[gate_b] = output_a
    output_to_input[output_a] = gate_b
    output_to_input[output_b] = gate_a

def compute(output, states, observed=frozenset()):
    a, op, b = output_to_input[output]
    if a in observed or b in observed:
        return None
    if a in output_to_input:
        a = compute(a, states, observed.union([a]))
    else:
        a = states[a]
    if a is None:
        return None
    if b in output_to_input:
        b = compute(b, states, observed.union([b]))
    else:
        b = states[b]
    if b is None:
        return None
    return ops[op](a, b)
    
def test_output(index):
    if index == 0:
        # test only primary bit
        for x, y in product(range(2), range(2)):
            states = {}
            insert("x", x, states)
            insert("y", y, states)
            expected_z = (x+y)&1
            actual_z = compute(f"z{index:02}", states)
            if actual_z != expected_z:
                return False
    elif index < 45:
        for x, y in product(range(4), range(4)):
            x = x << (index - 1)
            y = y << (index - 1)
            states = {}
            insert("x", x, states)
            insert("y", y, states)
            expected_z = ((x+y) >> index) & 1
            actual_z = compute(f"z{index:02}", states)
            if actual_z != expected_z:
                return False
    return True

def search(swapped: set, index=0):
    if index >= 46:
        return True
    if test_output(index):
        return search(swapped, index+1)
    correct_deps = frozenset()
    deps = resolve_dependencies(f"z{index:02}") - swapped
    if index > 0:
        correct_deps = resolve_dependencies(f"z{index-1:02}")
        deps = deps - correct_deps
    for a, b in product(deps, set(input_to_output) - correct_deps - swapped):
        swap(input_to_output[a], input_to_output[b])
        swapped.update([a, b])
        if test_output(index) and search(swapped, index+1):
            return True
        swapped.difference_update([a, b])
        swap(input_to_output[a], input_to_output[b])
    return False

swapped = set()
assert search(swapped)
print(",".join(sorted([input_to_output[x] for x in swapped])))
