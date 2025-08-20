from collections import Counter
from pqdict import pqdict
import sys
import time
from itertools import count
from tqdm import tqdm

inp = sys.stdin.read().rstrip()

graph = {}
for line in inp.split('\n'):
    a, b = line.split('-')
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)
graph = {k: frozenset(v) for k, v in graph.items()}

frozenset(frozenset())

t = time.time()
best = frozenset()
q = pqdict.maxpq()
q[(frozenset(), frozenset(graph))] = 1
duplicate_intersections = Counter()
it = iter(count())
while len(q) > 0 and q.topvalue() > len(best):
    (g, intersections), length = q.popitem()
    best = max(best, g, key=len)
    for node in sorted(intersections):
        i = next(it)
        new_g = g.union([node])
        new_intersections = intersections.intersection(graph[node])
        q[(new_g, new_intersections)] = len(new_g) + len(new_intersections)
t = time.time() - t
print(",".join(sorted(best)))
print(t, i)
