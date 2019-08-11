"""
根据前序遍历和后序遍历
重构二叉树

"""
class TreeNode(object):
    def __init__(self,val):
        self.val =val
        self.left=None
        self.right =None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return 
        root = TreeNode(pre[0])
                
        index = tin.index(pre[0])
        left_pre = pre[1:index+1]
        right_pre = pre[index+1:]
        root.left = self.reConstructBinaryTree(left_pre,tin[:index])
        root.right = self.reConstructBinaryTree(right_pre,tin[index+1:])
        return root
        