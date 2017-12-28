# Python 2.7.1
# Algoritms for weighted directed graphs
# Graph input: A dictionary, where keys are all the nodes from 1 to n and values are lists of edges.
# Edges are in the form defined by the class Edge (Edge objects).


class Edge:
    v = -1  # target node
    weight = -1  # weight of the edge

    def __init__(self, u, w):
        self.v = u
        self.weight = w


# Computes the shortest distances in a directed graph. No negative cycles. Distances are computed until a target node is
# reached or until there is no further connection to unvisited nodes. Returns the sortest distances in a list.
def dijkstra(graph, start, target):
    assert isinstance(graph, dict)
    n = graph.__len__()
    distance = [float("inf")] * n
    distance[start - 1] = 0
    x = 0
    unvisited = set()
    for u in graph:
        unvisited.add(u)
    current = start
    while unvisited.__len__() > 0:
        edges = graph[current]
        for i in edges:
            x = distance[current - 1] + i.weight
            if distance[i.v - 1] > x:
                distance[i.v - 1] = x
        unvisited.discard(current)
        dist_min = float("inf")
        for u in unvisited:
            if distance[u - 1] < dist_min:
                dist_min = distance[u - 1]
                current = u
        if dist_min == float("inf"):
            return distance
        if current == target:
            return distance


# Computes and returns the reverse of a given directed weighted graph.
def reverse(graph):
    assert isinstance(graph, dict)
    r = {}
    for u in graph:
        r[u] = []
    for u in graph:
        for e in graph[u]:
            r[e.v].append(Edge(u, e.weight))
    return r


# Tracebacks one optimal path from start node to target node. Parameter distance is the list returned by
# dijkstra(graph, start, target).
def path_traceback(graph, distance, target):
    assert isinstance(graph, dict)
    assert isinstance(distance, list)
    if distance[target - 1] == float("inf"):
        return "No path"
    r = reverse(graph)
    L = []
    current = target
    L.append(current)
    while distance[current - 1] > 0:
        for u in r[current]:
            if distance[current - 1] == u.weight + distance[u.v - 1]:
                current = u.v
                L.append(current)
                break
    L.reverse()
    return L


# Test input
graph1 = {1: [Edge(2, 1.5), Edge(3, 1.9), Edge(5, 20)], 2: [Edge(3, 5.2)],
          3: [Edge(4, 0.5)], 4: [Edge(5, 10), Edge(1, 1)], 5: []}
y = dijkstra(graph1, 1, 5)
print("Distances: " + str(y))

p = path_traceback(graph1, y, 5)
print("Shortest path from start to target: " + str(p))
