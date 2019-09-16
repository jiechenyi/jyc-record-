
"""

DFS
用 栈 来实现BFS
"""
graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E", "F"],
    "E": ["C","D"],
    "F": ["D"]
}

def DFS(graph,s):
    dfs=[]
    stack=[]
    stack.append(s)
    seen = set()
    seen.add(s)

    while stack:
        tmp = stack.pop()
        dfs.append(tmp)
        for p in graph[tmp]:
            if p not in seen:
                stack.append(p)
                seen.add(p)
    print(dfs)

DFS(graph,"A")


