# -*- coding: utf-8 -*-

_ = float("inf")

def dijkstra(graph, n):
    distances = [0] * n
    flags = [False] * n
    pre_nodes = [0] * n

    flags[0] = True
    k = 0
    for i in range(n):
        distances[i] = graph[k][i]

    #print distances
    #print

    for j in range(n-1):
        mini = _
        for i in range(n):
            if distances[i] < mini and not flags[i]:
                mini = distances[i]
                k = i

        if k == 0: #不连通
            return

        flags[k] = True

        for i in range(n):
            if distances[i] > distances[k] + graph[k][i]:
                distances[i] = distances[k] + graph[k][i]
                pre_nodes[i] = k

        #print k
        #print distances
        #print flags
        #print pre_nodes
        #print

    return distances, pre_nodes

if __name__ == '__main__':
    n = 6
    graph = [
        [0, 6, 3, _, _, _],
        [6, 0, 2, 5, _, _],
        [3, 2, 0, 3, 4, _],
        [_, 5, 3, 0, 2, 3],
        [_, _, 4, 2, 0, 5],
        [_, _, _, 3, 5, 0]
    ]

    distances, pre_nodes = dijkstra(graph, n)
    print 'distances:', distances
    print 'pre_nodes:', pre_nodes