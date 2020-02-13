"""
99.恢复二叉搜索树
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。
"""
# 这个会超时

def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """

    def helper(node, xia, shang):
        if not node:
            return
        helper(node.right, node, shang)
        helper(node.left, xia, node)

        if node.val <= xia.val:
            tmp = node.val
            node.val = xia.val
            xia.val = tmp

        if node.val >= shang.val:
            tmp = node.val
            node.val = shang.val
            shang.val = tmp

        helper(node.right, node, shang)
        helper(node.left, xia, node)

    xia = ListNode(-float("inf"))
    shang = ListNode(float("inf"))

    helper(root, xia, shang)
    return root

# 借助中序遍历

def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    pre = TreeNode(-float("inf"))

    first = None
    second = None

    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if pre.val > node.val:
            if not first:
                first = pre

                print(first.val)
            if first:
                second = node
                print(second.val)
            flag = 1
        pre = node
        node = node.right
    if first and second:
        tmp = first.val
        first.val = second.val
        second.val = tmp

