# from aoc import *
from functools import cache
import sys
inp = sys.stdin.read().rstrip()
# inp = """kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn"""

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

@cache
def search(start, connected=None):
    # add current node to the connected set
    connected = (connected or frozenset()) | frozenset([start])
    largest_set = connected
    # evaluate a neighbor of start
    for n in graph[start]:
        # ensure that neighbor is connected to everything in connected
        for cn in connected:
            # node isn't connected, can't add it.
            if cn not in graph[n]:
                break
        else:
            # node is connected to everything
            largest_set = max(largest_set, search(n, connected), key=lambda x: len(x))
    return largest_set

from tqdm import tqdm
largest_set = frozenset()
for a in tqdm(graph):
    largest_set = max(largest_set, search(a), key=lambda x: len(x))

print(",".join(sorted(largest_set)))
