"""
112.路径总和

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
"""

# 递归
def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """

    if not root:
        return False
    if root.val == sum and not root.left and not root.right:
        return True

    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

# 非递归(队列）

def hasPathSum(root,sum):
    if not root:
        return False

    que = [(root, sum)]

    while que:
        r, s = que.pop(0)

        if r.val == s and not r.left and not r.right:
            return True

        if r.left:
            que.append((r.left, s - r.val))
        if r.right:
            que.append((r.right, s - r.val))
    return False
