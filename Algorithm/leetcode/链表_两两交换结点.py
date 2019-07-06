
"""
两两交换结点


"""
## 递归
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        if head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        else:
            ## head.next 为空，没有可以交换的点了 ，直接返回 head
            return head
        