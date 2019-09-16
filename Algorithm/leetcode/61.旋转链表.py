"""
61.给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。


"""

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution(object):
    def rotateRight(self,head,k):
        if not head or not head.next:
            return head
        n = 1
        p = head
        while p.next:
            p = p.next
            n += 1
        m = n - k % n - 1 # 需要前进的步数

        p.next = head
        q = head
        while m > 0:
            q = q.next
            m -= 1
        tmp = q.next
        q.next = None
        return tmp


l =[1,2,3,4,5]
head = ListNode(l[0])
for i in range(1,len(l)):
    head.next = ListNode(l[i])
s = Solution()
s.rotateRight(head,2)






























