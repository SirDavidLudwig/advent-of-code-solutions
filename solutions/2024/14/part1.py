from aoc import *
from dataclasses import dataclass

n, m = size = farr([103, 101])

@dataclass
class Robot:
    pos: FrozenArray
    vel: FrozenArray

robots = []
for line in sys.stdin:
    j, i, vj, vi = ints(line)
    robots.append(Robot(farr([i, j]), farr([vi, vj])))


grid = np.zeros(size, dtype=int)
for i, robot in enumerate(robots, start=1):
    grid[*robot.pos] += 1

for _ in range(100):
    grid = np.zeros(size, dtype=int)
    for i, robot in enumerate(robots, start=1):
        robot.pos = (robot.pos + robot.vel) % size
        grid[*robot.pos] += 1
    
ans = 1

counts = [0, 0, 0, 0]
for robot in robots:
    if robot.pos[0] < n//2 and robot.pos[1] < m//2:
        counts[0] += 1
    elif robot.pos[0] < n//2 and robot.pos[1] > m//2:
        counts[1] += 1
    elif robot.pos[0] > n//2 and robot.pos[1] < m//2:
        counts[2] += 1
    elif robot.pos[0] > n//2 and robot.pos[1] > m//2:
        counts[3] += 1
print(np.prod(counts))