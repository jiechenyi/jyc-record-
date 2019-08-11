"""
2019.06.29
层序遍历
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 
        res = []
        seq = [root]
        tmp=[]
        current=1
        thenext =0
        while seq :
            node = seq.pop(0)
            tmp.append(node.val)
            current -= 1
            if node.left:
                seq.append(node.left)
                thenext+=1
            if node.right:
                seq.append(node.right)
                thenext +=1
            if current == 0:
                res.append(tmp)
                tmp =[]
                current = thenext
                thenext = 0
              
        return res

"""
前序遍历
"""
### 递归 
class Solution_(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        res=[]
        return self.help(res,root)
    def help(self,res,root):
        if not root:
            return 
        res.append(root.val)
        self.help(res,root.left)
        self.help(res,root.right)
        return res
## 非递归
class Solution__(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        node = root
        stack=[]
        res=[]
        while stack or node:
            while node:
                stack.append(node)
                res.append(node.val)                
                node = node.left
            node=stack.pop()
            node = node.right
        return res

"""
中序遍历
"""
### 非递归
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        stack=[]
        res=[]
        node=root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            res.append(node.val)
            node = node.right
        return res
### 递归

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        return self.help(root,res)
    def help(self,root,res):
        if not root:
            return 
        self.help(root.left,res)
        res.append(root.val)
        self.help(root.right,res)
        return res
"""
后序遍历
"""
## 非递归（根右左[::-1]）

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        node = root
        stack=[]
        res=[]
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.right
            node=stack.pop()
            node = node.left
        return res[::-1]
    

