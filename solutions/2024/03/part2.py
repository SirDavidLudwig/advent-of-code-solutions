from aoc import *

inp = sys.stdin.read()

matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", inp)

total = 0
parse = True
for m in matches:
    if m.startswith("don't"):
        parse = False
    elif m.startswith("do"):
        parse = True
    elif parse:
        a, b = map(int, re.findall(r'\d+', m))
        total += a*b

print(total)
