# from aoc import *
import re
import sys
ints = lambda x: list(map(int, re.findall(r"\d+", x)))

inp = sys.stdin.read().rstrip()

# inp = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

register_values = {}
a, program = inp.split('\n\n')
for k, v in zip("ABC", ints(a.replace('\n', ''))):
    register_values[k] = v
program = ints(program)

class Computer:
    def __init__(self, program):
        self.registers = {
            "A": 0,
            "B": 0,
            "C": 0
        }
        self.program = program
        self.ip = 0
        self.ops = dict(enumerate([
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ]))

    def run(self):
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip+1]
            output = self.ops[opcode](operand)
            if opcode == 5:
                yield output

    def combo_operand(self, operand):
        assert operand < 7
        if operand < 4:
            return operand
        return self.registers[chr(operand - 4 + ord("A"))]

    def adv(self, operand):
        """
        The adv instruction (opcode 0) performs division. The numerator is the value in the A
        register. The denominator is found by raising 2 to the power of the instruction's combo
        operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by
        2^B.) The result of the division operation is truncated to an integer and then written to
        the A register
        """
        self.registers["A"] = self.registers["A"] // (2**self.combo_operand(operand))
        self.ip += 2

    def bxl(self, operand):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's
        literal operand, then stores the result in register B.
        """
        self.registers["B"] = self.registers["B"] ^ operand
        self.ip += 2

    def bst(self, operand):
        """
        The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby
        keeping only its lowest 3 bits), then writes that value to the B register.
        """
        self.registers["B"] = self.combo_operand(operand) % 8
        self.ip += 2

    def jnz(self, operand):
        """
        The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A
        register is not zero, it jumps by setting the instruction pointer to the value of its literal
        operand; if this instruction jumps, the instruction pointer is not increased by 2 after this
        instruction.
        """
        if self.registers["A"] == 0:
            self.ip += 2
        else:
            self.ip = operand

    def bxc(self, operand):
        """
        The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then
        stores the result in register B. (For legacy reasons, this instruction reads an operand but
        ignores it.)
        """
        self.registers["B"] = self.registers["B"] ^ self.registers["C"]
        self.ip += 2

    def out(self, operand):
        """
        The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then
        outputs that value. (If a program outputs multiple values, they are separated by commas.)
        """
        self.ip += 2
        return self.combo_operand(operand) % 8

    def bdv(self, operand):
        self.registers["B"] = self.registers["A"] // 2**self.combo_operand(operand)
        self.ip += 2

    def cdv(self, operand):
        self.registers["C"] = self.registers["A"] // 2**self.combo_operand(operand)
        self.ip += 2


def search(program, current=0, depth=0):
    if depth == len(program):
        return current
    for v in range(current << 3, ((current << 3) | 7) + 1):
        c = Computer(program)
        c.registers["A"] = v
        output = list(c.run())
        if output == program[-(depth+1):]:
            found = search(program, v, depth+1)
            if found is not None:
                return found
    return None

a_value = search(program)

c = Computer(program)
c.registers["A"] = a_value
print(list(c.run()))

print("Done")
