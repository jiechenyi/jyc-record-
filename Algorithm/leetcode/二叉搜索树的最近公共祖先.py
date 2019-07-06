"""
2019.06.29
二叉搜索树最近的公共祖先
"""
## 递归
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        if p.val == root.val :
            return root
        elif q.val == root.val:
            return root
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif q.val>root.val and p.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<root.val and q.val>root.val:
            return root
        elif q.val<root.val and p.val>root.val:
            return root
        
## 非递归

class Solution_(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root==p:
            return p
        if root==q:
            return q
        while root:
            if p.val < root.val and q.val<root.val:
                root = root.left
            elif p.val > root.val and q.val >root.val:
                root = root.right
            else:
                return root
            