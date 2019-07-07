# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return 
        if n ==0:
            return 
        low = head
        fast = head
        i = 0
        while i<n-1: # 先让 fast 指针向前走n-1步 （到达第n个结点的位置
            if fast.next:
                fast = fast.next
                i +=1
            else:
                return 
        if fast.next:
            while fast.next.next: # 然后让 low 和 fast 一起开始一次走一步，这样，fast 和low
                                # 之间的距离 一直是n；直到 fast 走到了倒数第二个，这时low.next 就是 要删除的点

                fast = fast.next
                low = low.next
           
            low.next = low.next.next # 让low.next指向 low.next.next
            return head
        else:
            return head.next
            
            