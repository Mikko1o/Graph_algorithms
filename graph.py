# Python 2.7.1
# Algorithms for directed graphs
# Graphs should be written in dictionaries, for example {1: [2, 3], 2: [3], 3: []}


def depth_first_search(g, start):
    stack = []
    color = g.__len__() * ['w']
    stack.append(start)
    while stack.__len__() > 0:
        v = stack.pop()
        print(v)
        for u in g[v]:
            if color[u - 1] == 'w':
                color[u - 1] = 'g'
                stack.append(u)
        color[v - 1] = 'b'
#    print(color)

from collections import deque


def breath_first_search(g, start):
    queue = deque([])
    queue.append(start)
    color = g.__len__() * ['w']
    while queue.__len__() > 0:
        v = queue.popleft()
        for u in g[v]:
            if color[u - 1] == 'w':
                color[u - 1] = 'g'
                queue.append(u)
        color[v - 1] = 'b'
#    print(color)


def reverse_graph(g):
    reverse = {}
    for u in g:
        reverse[u] = []
    for u in g:
        for w in g[u]:
            reverse[w].append(u)
    return reverse


def topological_sort(g):
    L = []  # topological ordering
    S = []  # nodes with no incoming edges
    stack = []
    reverse = reverse_graph(g)
    for u in reverse:
        if reverse[u].__len__() == 0:
            S.append(u)
    while S.__len__() > 0:
        n = S.pop()
        L.append(n)
        for m in g[n]:
            stack.append(m)
        while stack.__len__() > 0:
            m = stack.pop()
            reverse[m].remove(n)
            if reverse[m].__len__() == 0:
                S.append(m)
    for m in reverse:
        if reverse[m].__len__() > 0:
            return -1  # g has a cycle
    return L


# testing
graph1 = {1: [2, 3], 2: [3, 5], 3: [5], 4: [1], 5: [6], 6: [], 7: [4]}
# print(reverse_graph({1:[2], 2:[3,4], 3:[], 4:[]}))
# breath_search(graph1, 1)
# breath_search(graph1, 5)

l = topological_sort(graph1)
print(l)

g2 = {1: [2], 2: [3, 4], 3: [], 4: []}
print(topological_sort(g2))

g3 = {'a': ['b', 'c'], 'b':['c'], 'c':[]}
print(topological_sort(g3))
# depth-first search
