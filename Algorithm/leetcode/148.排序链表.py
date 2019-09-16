"""
148.在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

对链表进行归并排序
先递归地分割
再merge

"""

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        mid = tmp
        slow.next = None  # save and cut
        # recursive for cutting
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, left, right):

        res = ListNode(0)
        h = res

        # merge
        while left and right:
            if left.val < right.val:

                h.next = left
                left = left.next
                h = h.next
            else:

                h.next = right
                right = right.next
                h = h.next
        if left:
            h.next = left
        else:
            h.next = right
        return res.next
