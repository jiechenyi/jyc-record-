"""
95.不同的二叉搜索树II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def generateTrees(n):
    if n == 0:
        return

    def solve(l, r):
        res =[]
        if l > r:
            res.append(None)
            return res
        for i in range(l, r + 1):

            left = solve(l, i - 1)
            right = solve(i + 1, r)

            for lr in left:
                for rr in right:
                    cur = TreeNode(i)
                    cur.left = lr
                    cur.right = rr
                    res.append(cur)
        return res

    return solve(1,n)










