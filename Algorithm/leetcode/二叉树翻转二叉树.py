"""
2019.06.29
反转二叉树
"""

## 递归


class Solution(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        stack=[root]
        while stack:
            node = stack.pop(0)  
            if node:
                tmp = node.right
                node.right = node.left
                node.left = tmp
                stack.append(node.right)
                stack.append(node.left)
        return root