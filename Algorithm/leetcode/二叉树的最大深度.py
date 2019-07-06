"""
2019.06.29
"""

### 递归
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.right),self.maxDepth(root.left))+1

### 非递归

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack=[[1,root]]
        res = 0
        while stack:
            cur,node = stack.pop()
            
            
            if node.right:
                stack.append([cur+1,node.right])
            if node.left:
                stack.append([cur+1,node.left])
            res = max(res,cur)
        return res

            