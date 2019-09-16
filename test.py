# 新浪笔试
b= [1,2,4,3,2,1]
n =len(b)
cnt=0
tmp =[]
while b:
    min_num = min(b)
    index = b.index(min_num)
    if min_num not in tmp:
        tmp.append(min_num)
        b.pop(index)
    else:
        b[index] +=1
        cnt +=1


# BFS

graph = {
    "A": ["B","C"],
    "B": ["A","C","D"],
    "C": ["A","B","D","E"],
    "D": ["B","C","E", "F"],
    "E": ["C","D"],
    "F": ["D"]
 }

def BFS(graph,start):
    queque =[]
    queque.append(start)

    res =[]

    seen=set()
    seen.add(start)
    while queque:
        node = queque.pop(0)
        res.append(node)
        for p in graph[node]:
            if p not in seen:
                queque.append(p)
                seen.add(p)


    return res


# DFS
def DFS(graph,start):
    stack = []
    stack.append(start)

    res =[]
    seen = set()
    seen.add(start)

    while stack:
        node = stack.pop()

        res.append(node)

        for p in graph[node]:
            if p not in seen:
                seen.add(p)
                stack.append(p)

    return res

# Dijkstra(based on bfs)


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

def dijkstra(graph,start):

    pqueque = []
    heapq.heappush(pqueque,(0,start))

    seen = set()
    seen.add(start)

    distance = {}
    for node in graph:
        distance[node] = math.inf
    distance[start] = 0
    while pqueque:
        pair = heapq.heappop(pqueque)
        dist = pair[0]
        node = pair[1]
        seen.add(node)

        for p in graph[node]:
            if p not in seen:
                d = dist + graph[node][p]
                if d < distance[p]:
                    heapq.heappush(pqueque,(d,p))
                    distance[p] = d
    return distance





# 招行笔试 编程第一题
s="RRLRL"
def f(s):
    n = len(s)
    res=[0]*n
    i = 0


    while i < n: # 对于第i个字母
        step= 0
        if s[i] =="R":
            for m in range(i+1,n):# 从第i个开始 找到第一个不一样的
                if s[m] != s[i]:
                    break
                else:
                    step +=1
            if step == 0:

                res[i] +=1
            elif step % 2 ==0:
                res[m-1] +=1
            elif step%2 != 0:
                res[m] +=1
        else:
            for m in range(i-1,-1,-1):
                if s[m]!= s[i]:
                    break
                else:
                    step+=1
            if step == 0:
                res[i] +=1

            elif step%2 == 0:
                res[m+1] +=1
            elif step % 2 != 0:
                res[m] +=1
        i +=1
    print(res)




s='2??'
def qumo(s):
    n = len(s)
    min_num = int(s.replace("?","0"))
    max_num = int(s.replace("?","9"))
    cnt = 0

    for nu in range(min_num,max_num+1):
        if nu %13 == 5:
            cnt +=1
    print(cnt%(10**9+7))


# heap sort 复习

# 调整堆

def heapify(arr,n,i):
    if n>i:
        c1 = 2*i +1
        c2 = 2*i +2

        max_index = i

        if c1 < n and arr[c1] > arr[max_index]:
            max_index = c1
        if c2 < n and arr[c2] > arr[max_index]:
            max_index = c2
        if max_index != i:
            tmp = arr[i]
            arr[i] = arr [max_index]
            arr[max_index] = tmp
            heapify(arr,n,max_index)
        return arr
    else:
        return

# 构建堆
def build_heap(arr,n):

    last = (n-1-1)//2

    for i in range(last,-1,-1):
        heapify(arr,n,i)
    return arr


# 堆排序

def heap_sort(arr):
    n = len(arr)
    build_heap(arr,n)

    for i in range(n-1,-1,-1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp

        build_heap(arr,i)
    return arr


# 归并排序

def merge(arr,l,m,r):
    left_size  = m-l+1
    right_size = r-m
    left = []
    right  =[]
    i = l
    while i <= m:
        left.append(arr[i])
        i+=1
    j = m+1
    while j <=r:
        right.append(arr[j])
        j+=1
    i = 0
    j = 0
    k = l

    while i<left_size and j < right_size :
        if left[i] >= right[j]:
            arr[k] = right[j]
            k +=1
            j +=1
        else:
            arr[k] = left[i]
            i +=1
            k +=1

    while i < left_size:
        arr[k] = left[i]
        i +=1
        k +=1
    while j < right_size:
        arr[k] = right[j]
        j +=1
        k +=1

    return arr

def merge_sort(arr,l,r):
    if l<r:
        m = (l+r) //2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        return merge(arr,l,m,r)

arr =[1,5,3,2,7,5,8,9]

l = 0
r = len(arr)-1


# 全排列
# 递归

arr=[1,2,3]
def printArray(arr,n):
    for i in range(n):
        print(arr[i])
    print("\n")
def savetolist(res,arr):
    res.append(arr)

def permutation(arr,l,r,res):

    if l == r:
        savetolist(res,arr)
    else:
        for i in range(l,r+1,1):
            # // swap(arr,0,i)
            tmp = arr[l]
            arr[l] = arr[i]
            arr[i] = tmp
            permutation(arr,l+1,r,res)
            # swap(arr,0,i)
            tmp = arr[l]
            arr[l] = arr[i]
            arr[i] = tmp
def main(arr):
    res=[]
    permutation(arr,0,len(arr)-1,res)
    print(res)

main(arr)




































