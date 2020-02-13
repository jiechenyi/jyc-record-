"""

111.二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

"""

# 非递归 （宽度优先遍历）
def minDepth(root):
    if not root:
        return 0

    que= [(root,1)]


    while que:
        r, d = que.pop(0)
        if r.left:
            que.append((r.left,d+1))

        if r.right:
            que.append((r.right, d+1))

        if not r.left and not r.right:

            return d

# 递归
def minDepth(root):
    if not root:
        return 0
    minDepth = 99999
    if not root.right and not root.left :
        return 1
    if root.right:
        minDepth = min(1+self.minDepth(root.right), minDepth)
    if root.left:
        minDepth = min(1+self.minDepth(root.left), minDepth)
    return minDepth





