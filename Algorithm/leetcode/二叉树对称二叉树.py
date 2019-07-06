"""
2019.06.29
判断二叉树 是否是对称的

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## 递归 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.ismirror(root,root)
    def ismirror(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root2 or not root1:
            return False
        if root1.val == root2.val:
            return True and self.ismirror(root1.left,root2.right) and self.ismirror(root1.right,root2.left)

### 非递归

class Solution_(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack=[root,root]
        while stack:
            node1 = stack.pop(0)
            node2 = stack.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True
            