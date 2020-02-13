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


# 网易 第1题
# max（最大值的一半，和的1/3）

def eat(x):
    total = sum(x)
    max_num = max(x)


    if total % 3==0:
        print(total/3)
    else:
        print(int(total/3)+1)
x = [1,2,7]
print(eat(x))




# 第二题

def f(h,m,n):
    m = m+ h[0] # 将第一堆变成0
    tmp =[]
    tmp.append(0)

    for i in range(1,n):
        if h[i] == i:
            tmp.append(i)
            continue
        elif h[i] > i:
            m = m+ h[i] -i
            tmp.append(i)

        elif h[i] < i:
            if m >= (i-h[i]):
                m = m -(i-h[i])
                tmp.append(i)

            else:
                return False
    return True

h =[2,2,3,3,1]
m = 3
n = 5




# 第四题

def get_smallsum(arr):

    if not arr or len(arr) < 2:
        return 0
    return smallsum(arr,0,len(arr)-1)

def smallsum(arr,l,r):
    if l ==r :
        return 0
    mid = (l+r) >>1

    left = smallsum(arr,l,mid)
    right = smallsum(arr,mid+1,r)

    all = merge(arr,l,mid,r)

    return left + right +all


def merge(arr,l,mid,r):
    left = l
    right = mid +1
    res = []

    sum = 0


    while left <= mid and right <= r:

        if arr[left] <= arr[right]:
            res.append(arr[left])

            sum += arr[left] * (r-right +1)

            left +=1
        else:
            res.append(arr[right])
            right +=1
    res += arr[left:mid+1]
    res += arr[right:r+1]

    for i in range(l,r+1):
        arr[i] = res.pop(0)
    return sum


# print(get_smallsum(arr[::-1]))


# 第三题
def f(h,n,k):

    i = 0
    flag = True
    while i <n:
        next = i
        next_h = 0
        tmp = h[i+1:i+1+k]
        for j,num in enumerate(tmp):
            if num > h[i]:
                break
            elif num<h[i]:
                if num >= next_h:
                    next_h = num
                    next = i+j+1
        if next == i and flag ==True:
            next = i+k
            flag = False
        elif next ==i and flag ==False:
            return "NO"

        i = next
    return 'YES'

n = 5
k = 3
h = [6,2,4,3,8]




def binarysearch(arr,k):
    left,right = 0,len(arr)
    mid = (left + right )/2

    while left <= right:
        if arr[mid] == k:
            return mid
        if arr[mid] < k:
            left = mid+1

        else:
            right = mid -1
    return


def get_point(f,x,y):

    mid = (x+y) /2
    while x <= y :
         if f(mid) == 0 :
             return mid
         if f(mid) > 0:
             y = mid
         elif f(mid) < 0:
             x = mid
    return



a = [1,1,2,2,3,4,4,5,5,6,6]
n = len(a)
res =0
for i in range(n):
    res = res ^ a[i]







def quick_sort(arr,left,right):
    if left >= right:
        return
    start = left

    end = right

    key = arr[start]
    while start<end:
        while start <end and arr[end] > key:
            end -=1
        if start <end :
            arr[start] = arr[end]

            start +=1
        while start <end and arr[start] < key:
            start +=1
        if start <end :
            arr[end] = arr[start]
            end -=1
    arr[start] = key
    quick_sort(arr,left,start-1)
    quick_sort(arr,start+1,right)
    return arr















