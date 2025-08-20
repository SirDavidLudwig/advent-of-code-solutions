from aoc import *

inp = sys.stdin.read().rstrip()

inp = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

registers = {}
a, program = inp.split('\n\n')
for k, v in zip("ABC", ints(a.replace('\n', ''))):
    registers[k] = v

ip = 0
program = ints(program)
outputs = []

def combo_operand(operand):
    assert operand != 7
    if operand < 4:
        return operand
    operand -= 4
    return registers[chr(operand + 65)]

def adv(ip, operand):
    registers["A"] = registers["A"] // 2**combo_operand(operand)
    return ip + 2

def bxl(ip, operand):
    registers["B"] = registers["B"] ^ operand
    return ip + 2

def bst(ip, operand):
    registers["B"] = combo_operand(operand) & 7
    return ip + 2

def jnz(ip, operand):
    if registers["A"] == 0:
        return ip + 2
    return operand

def bxc(ip, operand):
    registers["B"] = registers["B"] ^ registers["C"]
    return ip + 2

def out(ip, operand):
    outputs.append(combo_operand(operand) & 7)
    return ip + 2

def bdv(ip, operand):
    registers["B"] = registers["A"] // 2**combo_operand(operand)
    return ip + 2

def cdv(ip, operand):
    registers["C"] = registers["A"] // 2**combo_operand(operand)
    return ip + 2

opcode_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]
    ip = opcode_map[opcode](ip, operand)

print(registers)

print(",".join(map(str, outputs)))
print("".join(map(str, outputs)))

# ans = 0
# incorrect 514051026
