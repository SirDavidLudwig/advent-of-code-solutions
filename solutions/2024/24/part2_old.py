from aoc import *
from itertools import count
import operator
import random

ops = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor
}

inp = sys.stdin.read().rstrip()

inp = inp.split('\n\n')
states = {}
for row in inp[0].split('\n'):
    k, v = row.split(': ')
    states[k] = int(v)

input_to_output = {}
output_to_input = {}
for row in inp[1].rstrip().split('\n'):
    a, op, b, _, c = row.split()
    node = (a, op, b)
    input_to_output[node] = c
    output_to_input[c] = node

def compute_value(key, states):
    result = 0
    for i in count():
        k = f"{key}{i:02}"
        if k not in states:
            break
        result |= states[k] << i
    return result

def number_to_states(key, value):
    return {f"{key}{i:02}": int(x) for i, x in enumerate(f"{value:045b}"[::-1])}

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
        raise Exception("Loop")
    if a in output_to_input:
        a = compute(a, states, observed.union([a]))
    else:
        a = states[a]
    if b in output_to_input:
        b = compute(b, states, observed.union([b]))
    else:
        b = states[b]
    return ops[op](a, b)

from itertools import combinations, product

# z00 depends on x-1, y-1, x00, y00

def test_output(index):
    assert index < 45
    for a, b in list(product([0, 1], [0, 1])):
        states = {
            **number_to_states("x", a << index),
            **number_to_states("y", b << index)
        }
        expected_sum = (a+b) & 1
        expected_carry = (a+b) >> 1
        # try:?
        z = compute(f"z{index:02}", states)
        if expected_sum != z or expected_carry != compute(f"z{index+1:02}", states):
            return False
        # except Exception:
        #     return False
    return True

# states = {
#     **number_to_states("x", random.randrange(2**45)),
#     **number_to_states("y", random.randrange(2**45)),
# }

# x = compute_value("x", states)
# y = compute_value("y", states)
# print(f"{x:046b}")
# print(f"{y:046b}")
# print(f"{x+y:046b}")
# print("".join([str(compute(f"z{i:02}", states)) for i in range(45, -1, -1)]))

# for i in range(44, -1, -1):
#     print('x' if not test_output(i) else ' ', end="")


def swap(output_a, output_b):
    gate_a = output_to_input[output_a]
    gate_b = output_to_input[output_b]
    input_to_output[gate_a] = output_b
    input_to_output[gate_b] = output_a
    output_to_input[output_a] = gate_b
    output_to_input[output_b] = gate_a

def search(swapped: set, i=0):
    output = f"z{i:02}"
    if output not in output_to_input:
        return True
    if test_output(i):
        return search(swapped, i+1)
    if len(swapped) == 8:
        return False
    prior_deps = frozenset() if i == 0 else resolve_dependencies(f"z{i-1:02}")
    for a, b in combinations(resolve_dependencies(output) - prior_deps, 2):
        a = input_to_output[a]
        b = input_to_output[b]
        if a in swapped or b in swapped:
            continue
        if a in output_to_input[b] or b in output_to_input[a]:
            continue
        swap(a, b)
        swapped.update([a, b])
        if search(swapped, i):
            return True
        swapped.difference_update([a, b])
        swap(a, b)
        # swap(output, other)
        # if test_output(i):
        #     swapped.update([output, other])
        #     print("Trying", swapped)
        #     if search(i+1, swapped):
        #         return True
        #     swapped.difference_update([output, other])
        # swap(output, other)
    return False

output = set()
print(search(output))

# for i in range(45):
#     output = f"z{i:02}"
#     if not test_output(i):
#         print("Swapping", i)
#         for other in output_to_input:
#             swap(output, other)
#             if test_output(i):
#                 print("Swapped")

#             swap(output, other)
#         assert test_output(i)


# print(test_output(0))
# print(test_output(0))
# x = input_to_output.copy()
# y = output_to_input.copy()
# original_output = "z00"
# original_gate = output_to_input[original_output]
# for other_gate, other_output in input_to_output.items():
#     if other_output == original_output:
#         # don't swap with itself
#         continue
#     # swap
#     input_to_output[other_gate], input_to_output[original_gate] = original_output, other_output
#     output_to_input[other_output], output_to_input[original_output] = original_gate, other_gate
#     if test_output(0):
#         print("Found")
#     # swap back
#     input_to_output[other_gate], input_to_output[original_gate] = other_output, original_output
#     output_to_input[other_output], output_to_input[original_output] = other_gate, original_gate
# print(resolve_dependencies("z00"))

# 00000

# 00 05
# 


# print(len(bin(1 << 45)[2:]))

# print(resolve_dependencies("z00"))

# def add(x, y):
#     states = {}
#     states |= number_to_states(x, "x")
#     states |= number_to_states(y, "y")

#     q = []
#     for row in inp[1].rstrip().split('\n'):
#         a, op, b, _, c = row.split()
#         q.append((a, op, b, c))

#     ops = {
#         "AND": operator.and_,
#         "OR": operator.or_,
#         "XOR": operator.xor
#     }

#     while len(q) > 0:
#         a, op, b, c = q.pop(0)
#         if a not in states or b not in states:
#             q.append((a, op, b, c))
#             continue
#         states[c] = ops[op](states[a], states[b])
    
#     return compute_value("z", states)

# x, y = 0, 1
# z = add(x, y)
# print(f"{x:045b}")
# print(f"{y:045b}")
# print(f"{z:045b}")

# ans = 0

# print(x := compute_value("x"))
# print(y := compute_value("y"))
# a = bin(x+y)
# b = bin(compute_value("z"))
# print(a)
# print(b)
# print("".join(['x' if a != b else ' ' for a, b in zip(a, b)]))

# print(ans)
