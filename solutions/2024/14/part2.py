from aoc import *
from dataclasses import dataclass, field
from copy import deepcopy

dir(cards=True, diags=True)

n, m = size = farr([103, 101])

with open("./input/puzzle.txt") as f:
    inp = f.read().rstrip()

@dataclass(unsafe_hash=True)
class Robot:
    id_: field(hash=True)
    pos: FrozenArray = field(hash=False)
    vel: FrozenArray = field(hash=False)

robots = {}
for i, line in enumerate(inp.split("\n")):
    j, i, vj, vi = ints(line)
    robot = Robot(i, farr([i, j]), farr([vi, vj]))
    if tuple(robot.pos) not in robots:
        robots[*robot.pos] = []
    robots[*robot.pos].append(robot)

def floodfill(pos):
    q = []
    found = set()
    if tuple(pos) in robots:
        q.append(pos)
    while len(q) > 0:
        p = q.pop()
        if tuple(p) in found:
            continue
        found.add(tuple(p))
        for d in map(dir.delta, dir):
            np = p + d
            if tuple(np) not in robots or tuple(np) in found:
                continue
            q.append(np)
    return found

best_found = None
from tqdm import tqdm
for s in tqdm(range(1, 20000)):
    grid = np.zeros(size, dtype=int)
    state = []
    next_robots = {}
    for i, robot in enumerate([robot for group in robots.values() for robot in group], start=1):
        robot.pos = (robot.pos + robot.vel) % size
        if tuple(robot.pos) not in next_robots:
            next_robots[tuple(robot.pos)] = []
        next_robots[*robot.pos].append(robot)
        grid[*robot.pos] += 1
    robots = next_robots

    observed = set()
    best = None
    for pos in robots:
        if tuple(pos) in observed:
            continue
        found = floodfill(pos)
        if best is None or len(found) > len(best):
            best = found
        observed |= found

    if best_found is None or len(best) > best_found[1]:
        best_found = (s, len(best))
        print()
        print()
        for line in grid:
            print("".join([' ' if c == 0 else '#' for c in line]))
        print(best_found)
        print()
        print()
