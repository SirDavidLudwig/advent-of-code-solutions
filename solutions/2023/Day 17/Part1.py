import sys
sys.path.append("../../../common")
from aoc import *
import numpy as np
from tqdm import tqdm
import time

with open("../puzzle_inputs/17.txt") as f:
    lines = f.readlines()

grid = np.array([[int(c) for c in line.strip()] for line in lines])
goal = np.array(grid.shape) - 1

def neighbors(state):
    pos, direction, moves = state
    result = []
    for dir, delta in dirs(deltas=True):
        npos = pos + delta
        if revdir(dir) == direction:
            continue
        if np.any(npos < 0) or np.any(npos >= grid.shape):
            continue
        nmoves = 1 if direction != dir else moves+1
        if nmoves > 3:
            continue
        cost = grid[(*npos,)]
        new_state = (tuple(npos), dir, nmoves)
        result.append((cost, new_state))
    return result

def heuristic(state):
    return np.linalg.norm(state[0] - (goal - 1), ord=1)

t = time.time()
for (cost, state, _) in tqdm(astar(((0, 0), '', 0), neighbors, heuristic)):
    if np.all(state[0] == goal):
        print(cost)
        break
time.time() - t
