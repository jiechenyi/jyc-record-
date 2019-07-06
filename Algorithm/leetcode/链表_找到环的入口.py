"""
判断链表中是否有环或者找到环的入口
2019.07.02

"""

## 双指针

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or head.next == None or head.next.next ==None:
            return False
        pre = head.next.next  ## 快指针一次走两步
        cur = head.next  ## 慢指针一次走一步
        while pre != cur:  ## 两个指针相遇之后，慢指针回到头结点
            if pre.next == None or pre.next.next == None:
                return False
            pre = pre.next.next
            cur = cur.next
        
        pre = head
        while pre!=cur:  ## 两个指针一次走一步，再次相遇的点就是环的入口
            pre = pre.next
            cur = cur.next
        return True
            
            