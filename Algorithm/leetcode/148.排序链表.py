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

def sort(head):
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
    left = sort(head)
    right = sort(mid)
    res = ListNode(0)
    h =res

    # merge
    while left and right:
        if left.val < right.val:

            h.next = left
            left = left.next
        else:

            h.next =right
            right = right.next
    if left :
        h.next = right
    else:
        h.next = right
    return res.next



class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

