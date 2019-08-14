"""
61.给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。


"""

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution(object):
    def rotateRight(self,head,k):
        if not head:
            return
        for i in range(k):
            head = self.help(head)
        return head

    def help(self,head):
        if not head:
            return

        p = head
        while p.next.next :
            p = p.next
        tmp = p.next

        tmp.next = head
        p.next  = None
        return head




























