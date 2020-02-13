"""
86.分隔链表

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置
"""

# 先拆后并
def partition(head,x):
    p = ListNode("p")
    q = ListNode("q")
    p_ = p
    q_ = q
    while head:
        if head.val < x:
            p.next = ListNode(head.val)

            p = p.next
        else:
            q.next = ListNode(head.val)
            q = q.next
        head = head.next

    p.next = q_.next

    return p_.next

def partition(head,x):

    before =before_head= ListNode(0)
    after = after_head=ListNode(0)

    while head:
        if head.val < x:
            before.next  =head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    after.next =None  # 这句话不能少 定义一个链表 最后要定义尾部指向 None


    before.next = after_head.next

    return before_head.next


def partition(head,x):
    p = ListNode("key")
    p.next = head
    res = ListNode("head")
    res.next = p
    mid = res
    flag = p
    while head:
        if head.val < x:

            tmp = head.next
            head.next = p
            mid.next = head
            flag.next = tmp
            head = p.next
            mid = mid.next
            flag = p
        else:
            flag = head
            head = head.next

    mid = res
    while mid.next:
        if mid.next.val == "key":
            if mid.next.next:
                mid.next = mid.next.next
            else:
                mid.next = None
        else:
            mid = mid.next

    return res.next




