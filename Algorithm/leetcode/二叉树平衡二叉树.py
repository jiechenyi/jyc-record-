"""
判断是否是平衡二叉树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        if abs(left-right) > 1:
            return False
        else:
            return True and self.isBalanced(root.right) and self.isBalanced(root.left)
            
    def maxdepth(self,root):
        if not root:
            return 0
        return max(self.maxdepth(root.right),self.maxdepth(root.left))+1
            
        