"""
116.填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

"""

# 非递归 使用 que
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

# 非递归 使用常量空间

def connect(root):
    if not root:
        return
    pre = root
    while pre:
        cur =  pre
        while cur:
            if cur.left:
                cur.left.next = cur.right
            if cur.right and cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        pre = pre.left
    return root
# 递归

def connect(root):
    if not root:
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
    connect(root.left)
    connect(root.right)
    return root




