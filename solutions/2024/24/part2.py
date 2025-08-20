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

def swap(output_a, output_b):
    gate_a = output_to_input[output_a]
    gate_b = output_to_input[output_b]
    input_to_output[gate_a] = output_b
    input_to_output[gate_b] = output_a
    output_to_input[output_a] = gate_b
    output_to_input[output_b] = gate_a

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
            # expected_carry = ((x+y)&2) >> 1
            # actual_carry = compute(f"z{index+1:02}", states)
            # if actual_z != expected_z or actual_carry != expected_carry:
            #     return False

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
            # expected_carry = ((x+y) >> (index + 1)) & 1
            # actual_carry = compute(f"z{index+1:02}", states)
            # if actual_z != expected_z or actual_carry != expected_carry:
            #     return False
    return True
  
pairs = [
    ("gwh", "z09"),
    ("wbw", "wgb"),
    ("rcb", "z21"),
    ("jct", "z39")
]
for pair in pairs:
    swap(*pair)

# unexplored_gates = set(input_to_output)
# correct_gates = set()
for i in range(46):
    output = f"z{i:02}"
    # print(output)
    if not test_output(i):
        print(output, "incorrect")
        break
    # correct_gates.update(resolve_dependencies(output))
else:
    print("All correct")
print(",".join(sorted([x for pair in pairs for x in pair])))

# print(len(unexplored_gates - correct_gates))