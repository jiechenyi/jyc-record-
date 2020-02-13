"""
129.求根到叶子节点数字之和

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和


"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b  = TreeNode(2)
c = TreeNode(3)
e = TreeNode(4)

a.right = c
a.left = b



def sumNumbers(root):
    res=0
    cur=""

    def helper(root):
        nonlocal cur
        nonlocal res
        if not root:
            return
        cur += str(root.val)

        if not root.left and not root.right:
            res += int(cur)
        else:
            helper(root.left)
            helper(root.right)
        cur = cur[:-1]

    helper(root)

    return res





print(sumNumbers(a))

