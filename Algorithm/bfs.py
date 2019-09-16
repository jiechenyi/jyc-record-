
"""

BFS
用队列来实现BFS
"""
graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E", "F"],
    "E": ["C","D"],
    "F": ["D"]
 }

def BFS(graph,s):
    bfs =[]
    que = [s]
    seen=set()
    seen.add(s)
    while que:
        tmp = que.pop(0)
        bfs.append(tmp)

        for p in graph[tmp]:
            if p not in seen:
                que.append(p)
                seen.add(p)
    print(bfs)

BFS(graph,"E")


def BFS_tree(graph,s):
    bfs =[]
    que = [s]
    seen=set()
    seen.add(s)
    parent={s:None}
    while que:
        tmp = que.pop(0)
        bfs.append(tmp)
        for p in graph[tmp]:
            if p not in seen:
                que.append(p)
                seen.add(p)
                parent[p]=tmp
    print(bfs)
    print(parent)
    return parent

parent = BFS_tree(graph,"E")

# 从根出发到node  最短路径

def minRoad(parent,node):
    cnt=0
    while node:
        print(node)
        node = parent[node]
        cnt +=1
    print(cnt)
minRoad(parent,"B")







