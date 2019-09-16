"""
最短路径：
边都是有权重的，两个node之间的最短路径

利用 优先队列 实现
"""

# BFS

import heapq # python 自带的 优先队列
import math
graph = {
    "A": {"B":5,"C":1},
    "B": {"A":5,"C":2,"D":1},
    "C": {"A":1,"B":2,"D":4,"E":8},
    "D": {"B":1,"C":4,"E":3, "F":6},
    "E": {"C":8,"D":3},
    "F": {"D":6}
 }

def init_distance(graph,s):
    distance={}

    for node in graph:
        distance[node] = math.inf
    distance[s] = 0
    return distance

def dijkstra(graph,s):

    pque = []
    heapq.heappush(pque,(0,s))
    seen = set()
    seen.add(s)

    distance =init_distance(graph,s)
    while pque:
        pair = heapq.heappush(pque)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()

        for p in nodes:
            if p not in seen:
                d = dist+graph[vertex][p]
                if d<distance[p]:  # 更新pque 中的距离
                    heapq.heappush(pque,(d,p))

                    distance[p] = dist + graph[vertex][p]

    return distance



def dijkstra_test(graph,s):
    pqueque =[]
    distance=init_distance(graph,s)
    heapq.heappush(pqueque,(0,s))

    seen=set()
    seen.add(s)

    while pqueque:
        pair = heapq.heappop(pqueque)
        dist = pair[0]
        vertex =  pair[1]

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                d = dist + graph[vertex][w]
                if d < distance[w]:
                    heapq.heappush(pqueque,(d,w))
                    distance[w] = d
    return distance

print(dijkstra_test(graph,"A"))


























