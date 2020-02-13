"""
113.路径总和II

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。
"""


# 递归
def pathSum(root, sum):
    res=[]
    cur =[]

    def dfs(root,cur, cur_sum):
        if root and not root.left and not root.right:
            print(root.val)
            cur_sum += root.val
            if cur_sum == sum:
                cur.append(root.val)
                res.append(cur[:])

        elif root:
            print(root.val)

            dfs(root.left, cur+[root.val], cur_sum+root.val)

            dfs(root.right, cur+[root.val], cur_sum+root.val)


    dfs(root, cur, 0)
    return res

# 非递归

def pathSum2(root,sum):
    res=[]

    stack=[(root,[],0)]

    while stack:
        node, cur, cur_sum = stack.pop()
        if node and not node.right and not node.left:
            cur_sum += node.val
            if cur_sum == sum:
                cur.append(node.val)
                res.append(cur)
        if node and node.left:
            stack.append((node.left, cur+[node.val], cur_sum+node.val))
        if node and node.right:
            stack.append((node.right, cur+[node.val], cur_sum+node.val))
    return res

# 回溯

def pathSum3(root,sum):
    res = []
    cur = []

    if not root and sum == 0:
        return []

    def dfs(root, cur_sum):
        nonlocal cur
        nonlocal res  # 这两句是必要的吗
        if not root:
            return
        cur.append(root.val)
        cur_sum += root.val
        if not root.left and not root.right and cur_sum == sum:
            res.append(cur[:])
        else:
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
        cur.pop()
        cur_sum -= root.val

    dfs(root, 0)
    return res




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# a = TreeNode(5)
# b = TreeNode(4)
# c = TreeNode(8)
# d = TreeNode(11)
# e = TreeNode(13)
# f = TreeNode(4)
# g = TreeNode(7)
# h = TreeNode(2)
# i = TreeNode(5)
# j = TreeNode(1)
#
# a.left = b
# a.right = c
#
# b.left = d
# c.left = e
# c.right = f
#
# d.left = g
# d.right = h
#
# f.left = i
# f.right = j

a= TreeNode(-2)
b = TreeNode(-3)
a.right = b

# print(pathSum(a, -5))
print(pathSum3(a,-5))

