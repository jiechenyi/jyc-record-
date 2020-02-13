"""

98.验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。



"""
# 判断中序遍历之后的序列是否为递增的

def isValidBST(root):
    if not root:
        return
    def helper(root,res):
        if not root:
            return
        helper(root.left,res)
        res.append(root.val)
        helper(root.right,res)
        return res
    res = helper(root,[])

    for i in range(len(res)):
        if i>0 and res[i]<= res[i-1]:
            return False
    return True

# 递归

def isValidBST(root):



    def helper(node,xia=-float('inf'),shang=float('inf')):
        if not node:
            return True

         val = node.val

        if val <= xia or val >= shang:
            return False
        if not helper(node.right, xia = val, shang = shang):
            return False
        if not helper(node.left, xia = xia, shang = val):
            return False
        return True

    return helper(root)

# 迭代 （将上面的尾递归改成迭代）
def isValidBST(root):
    if not root:
        return True

    que = [(root,-float('inf'),float('inf'))]

    while que:
        node,xia,shang = que.pop(0)
        if not node:
            continue
        if node.val <= xia or node.val >=shang:
            return False
        if node.right:
            que.append((node.right,node.val, shang))
        if node.left:
            que.append((node.left, xia,node.val))
    return True
