from aoc import *

inp = sys.stdin.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", inp)

total = 0
for m in matches:
    a, b = map(int, m)
    total += a*b

print(total)
