from aoc import *

inp = sys.stdin.read().rstrip()

graph = {}

ans = 0
for line in inp.split('\n'):
    a, b = line.split('-')
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

def find_cycle(start):
    for n1 in graph[start]:
        for n2 in graph[n1]:
            if start in graph[n2]:
                result = frozenset([start, n1, n2])
                yield result

ans = 0
seen = set()
for g in graph:
    for group in find_cycle(g):
        if group in seen:
            continue
        seen.add(group)
        for n in group:
            if n.startswith('t'):
                ans += 1
                break

print(ans)
