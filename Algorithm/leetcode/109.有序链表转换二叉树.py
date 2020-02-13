"""

109.有序链表转化二叉树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1

"""

# 将链表中的指存到数组里 用空间来换时间 因为数组的查找只需要O(1)

def sortedListToBST(head):
    arr =[]

    while head:
        arr.append(head.val)
        head = head.next

    def helper(arr):
        n = len(arr)
        if len(arr) < 1:
            return
        root = TreeNode(arr[n//2])
        root.left = helper(arr[:n//2])
        root.right = helper(arr[n//2:])
        return root
    root =helper(arr)
    return root

# 快慢指针找到链表的中点
# 双指针


def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findmid(head, tail):
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        return slow

    def helper(head, tail):
        if head == tail: return
        node = findmid(head, tail)
        root = TreeNode(node.val)
        root.left = helper(head, node)
        root.right = helper(node.next, tail)
        return root

    return helper(head, None)


# 有错误的

class Solution:

    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node


# 仿照中序遍历构造

def sortedListToBST(head):
    size = 0
    p = head
    while p:
        size += 1
        p = p.next
    def rebuildTree(l,r):
        nonlocal head
        if l>= r:
            return None
        mid = (l+r)//2
        left = rebuildTree(l,mid)
        root = TreeNode(head.val)
        root.left = left

        head = head.next

        root.right = rebuildTree(mid+1, r)
        return root
    return rebuildTree(0, size)



