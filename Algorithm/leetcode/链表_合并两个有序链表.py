

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l2:
                return l1
        if not l1:
            return l2
        pre=ListNode(-999999)
        res = pre
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res=res.next
                l2 = l2.next
        if l1:
            res.next = l1
        if l2 :
            res.next = l2
        return pre.next
# 递归

class Solution_(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 :
            return l2
        if not l2:
            return l1
        head = ListNode(-999999)
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next,l2)
           
        else:
            head = l2
            head.next = self.mergeTwoLists(l1,l2.next)
           
        return head