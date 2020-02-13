"""
117。填充每个节点的下一个右侧节点指针II
与上一题相比 没有说叶子节点都在同一层

"""

# 非递归 使用 que
# 这种记录行号的方法 两题都可以用
def connect(root):
    if not root:
        return

    que = [(root, 1)]
    start = 0
    pre = None
    while que:
        node, depth = que.pop(0)
        if start != depth:
            node.next = None
        else:
            node.next = pre
        if node.right:
            que.append((node.right, depth + 1))
        if node.left:
            que.append((node.left, depth + 1))
        start = depth
        pre = node
    return root

# 常数空间的话（懒得看了）

def connect(root):
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            tail = None
        return root
