"""
114.将二叉树展开为链表
给定一个二叉树，原地将它展开为链表。
"""



def flatten(root):

    while root:
        if not root.left:
            root = root.right
        else:
            most_right = root.left

            while most_right.right:
                most_right = most_right.right

            tmp = root.right

            root.right = root.left
            most_right.right = tmp
            root.left = None

            root = root.right

# 后序遍历 的变体 右->左->根

def flatten(root):
    stack =[root]

    pre = None
    while stack:
        node = stack.pop()
        if pre:
            pre.right = node
            pre.left = None
        if node :
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            pre = node













