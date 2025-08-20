import heapq
import numpy as np

def csv(*x, delim=",", dtype=int):
	result = np.array([list(map(dtype, s.strip().split(delim))) for s in x])
	if len(result) == 1:
		return result[0]
	return result

def find_edges(dist):
	edges = []
	for a in range(len(dist)):
		for b in range(a+1, len(dist)):
			heapq.heappush(edges, (dist[a][b], a, b))
	return edges

def kruskal(dist, edge_q=None):
	forests = [set([v]) for v in range(len(dist))]
	if edge_q is None:
		edge_q = find_edges(dist)
	found = []
	while len(forests[0]) != len(dist):
		(weight, a, b) = heapq.heappop(edge_q)
		if forests[a] is not forests[b]:
			forests[a].update(forests[b])
			found.append((weight, a, b))
			for v in forests[b]:
				forests[v] = forests[a]
	return found
