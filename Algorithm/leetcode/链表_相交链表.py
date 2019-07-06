"""
2019.07.02
找到链表相交的点

"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        
        while pa!=pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa

## 计算长度
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    
    """
    if not headA or not headB:
        return 
    a = headA
    b = headB
    n = 0
    m = 0 #
    ## 分别计算两个链表的长度
    while a:
        a = a.next
        n = n+1
    while b:
        b = b.next
        m = m+1
    a = headA
    b = headB
    while a or b:
        if a == b:
            return a
        if n ==m: ## 长度相等的话，每个都走一步 肯定会相遇
            a=a.next
            b = b.next
        elif n>m: ## 说明a 的在交点前的长度比较长，那就让a先走几步
            a=a.next
            n -=1
        else:
            b = b.next
            m -=1
    return 