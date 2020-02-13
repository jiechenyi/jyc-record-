"""

92.反转链表II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetweeen(head, m, n):
    dummy = ListNode(-1)
    dummy.next = head # 指向新链表的第一个节点
    first = dummy # 第一段的最后一个节点
    for i in range(1,m):
        first = first.next
    second = first.next #第二段最后一个节点

    if not second:
        return dummy.next

    l = second # 第二段第一个节点
    r = l.next # 第三段开始节点

    for i in range(m,n):
        tmp = r.next
        r.next = l
        l = r
        r = tmp

    first.next = l
    second.next = r
    return dummy.next





e = ListNode(5)
d= ListNode(4)
c = ListNode(3)
b = ListNode(2)
a = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
head = a
m = 2
n =4
print(reverseBetweeen(head,m,n))
