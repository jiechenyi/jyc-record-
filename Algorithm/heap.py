"""
一个完全二叉树可以用一个数组表示
将这个数组进行 heapify
然后可以利用这个技术进行 heap sort

"""

# 堆化
"""

     4        6
    / \  --> / \ 
   5   6    5   4

"""

def heapify(tree,n,i):  # n 是数组长度，i是需要调节的结点位置
    if n < i:
        return

    c1 = 2*i +1
    c2 = 2*i +2
    max_index = i

    #  和子结点中 最大的那个数进行交换
    if c1<n and tree[c1] > tree[max_index]:
        max_index= c1
    if c2<n and tree[c2] > tree[max_index]:
        max_index = c2
    if max_index != i:
        tmp = tree[i]
        tree[i] = tree[max_index]
        tree[max_index] = tmp
        heapify(tree,n,max_index)

    return tree
# tree=[4,10,3,5,1,2,6]
# print(heapify(tree,7,0))

# 构建堆
"""
从最后一个结点的 父结点开始，一个一个往前做堆化
构建堆
"""

def build_heap(tree,n):

    start = (n-1-1)//2

    for i in range(start,-1,-1):
        heapify(tree,n,i)
    return tree

tree=[4,10,3,5,1,2,6]
print(build_heap(tree,len(tree)))

# heap sort
"""
构建堆，然后第一个元素就是最大的
将其与最后一个元素进行交换，"并从arr中拿出去"，
然后再对剩下的进行 build heap

"""
"""
写堆排序的时候，要写三个函数
heapify
build_heap
heap_sort

"""
"""
整体的复杂度是 O(nlogn),无论最好最坏，平均都是这个
是一种不稳定的排序


"""

def heap_sort(tree):
    n = len(tree)
    tree = build_heap(tree,n)
    for m in range(n-1,-1,-1):
        tmp = tree[m]
        tree[m] = tree[0]
        tree[0] = tmp
        build_heap(tree,m)
    return tree

tree=[4,10,3,5,1,2,6]
print(heap_sort(tree))



