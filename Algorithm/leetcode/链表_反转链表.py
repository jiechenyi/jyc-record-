
"""
2019.07.01

翻转链表
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 非递归
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        p= None
        while head:
            tmp = head.next
            head.next = p
            p = head
            head= tmp
        return p
## 递归

class Solution_(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next) # head.next 已经reverse 好了
        head.next.next = head # 只需将 head 和 head.next 之间的箭头反向
        head.next=None
        return p
        






def f(head):
    if not head:
        return
    p = None
    while head:
        tmp=  head.next
        head.next= p
        p = head
        head = tmp
    return p