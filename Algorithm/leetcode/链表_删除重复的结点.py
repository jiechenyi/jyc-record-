"""

删除重复的结点使得其只出现一次
"""
class ListNode(object):
    def __init__(self,val):
        self.val= val
        self.next = None
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        p = head
        while p:
            if p.next:
                if p.val == p.next.val: # 如果当前结点的值和下一个结点的值相同，
                    p.next=p.next.next # 
                else:
                    p = p.next # 如果不相同，p继续前进
            else:
                p = p.next # p = None 结束
        return head


"""
结点不重复
"""
class Solution_(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        p = ListNode(-99999)
        p.next = head
        pre = p
        cur = head
     
        while cur:
            flag=False
            while cur.next and cur.val == cur.next.val:
                flag =True
                cur = cur.next
            if flag == True:
                pre.next = cur.next
                
            else:
                pre = cur
            cur = cur.next
        return p.next
    