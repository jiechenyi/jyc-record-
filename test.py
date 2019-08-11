def bs(arr,k):
    left = 0
    right = len(arr)
    
    while left <= right:
        mid = (left+right) //2
        if arr[mid] == k:
            return mid
        elif arr[mid]<k:
            left = mid+1
        else :
            right = mid-1
        return 
    
        
def bs2(arr,k,left,right):
    if left <=right:
        mid = (left + right)//2
        if arr[mid] == k:
            return mid
        if arr[mid] <k:
            return bs2(arr,k,mid+1,right)
        if arr[mid] >k:
            return bs2(arr,k,left,mid-1)




def inorder(root):

    stack=[]
    node = root
    res= []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right

    return res

def postorder(root):
    stack =[]
    node = root
    res =[]
    while stack or node:
        while node:
            stack.append(node)
            res.append(node.val)
            node = node.right
        node = stack.pop()
        node = node.left
    return res[::-1]


def lowest(root,p,q):
    if not root:
        return 
    if not p or q.val == root.val:
        return q
    if not q or p.val == root.val:
        return p
    while root:
        if q.val < root.val and p.val < root.val:
            root = root.left
        if q.val > root.val and p.val > root.val:
            root = root.left
        else:
            return root

def mergetree(root1,root2):
    if not root1:
        return root2
    if not root2:
        return root1
    root1.val =root1.val + root2.val
    root1.left = mergetree(root1.left,root2.left)
    root1.right = mergetree(root1.right,root2.right)
    return root1

def issymmetric(root):
    if not root:
        return True
    stack=[root,root]
    while stack:
        node1 = stack.pop(0)
        node2 = stack.pop(0)

        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
    return True

def isbalance(root):
    left = maxdepth(root.left)
    right = maxdepth(root.right)
    if abs(left-right) >1:
        return False

    else:
        return True and isbalance(root.left) and isbalance(root.right)

def maxdepth(root):
    stack=[(1,root)]
    node =root
    maxd = 1
    while stack:
        cur,node = stack.pop()
        if node.left:
            
            stack.append((cur+1,node.left))
            maxd = max(maxd,cur+1)
        if node.right:
            stack.append((cur+1,node.right))
            maxd = max(maxd,cur+1)
    return maxd

def lo(root,p,q):
    if not p :
        return q
    if not p:
        return q
    if p.val == root.val:
        return root
    if q.val == root.val:
        return root

    left =lo(root.left,p,q)
    right = lo(root.right,p,q)

    if left and right:
        return root
    if left :
        return left
    if right:
        return right 
            
def invert(root):
    if not root:
        return 
    tmp = root.left
    root.left = invert(root.right)
    root.right = invert(tmp)  
    return root      
def invert2(root):
    if not root:
        return 
    
    stack=[root]
    while stack:
        node = stack.pop(0)
        if node:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            stack.append(node.left)
            stack.append(node.right)
    return root

def movezero(arr):
    n= len(arr)
    pre = 0
    cur =1
    while pre<cur and cur<n:
        if arr[pre] != 0 and arr[cur] !=0:
            pre +=1
            cur +=1
        elif arr[pre] != 0 and arr[cur] == 0:
            pre +=1

            cur +=1
        elif arr[pre] == 0 and arr[cur] == 0:
            cur +=1
        elif arr[pre] ==0 and arr[cur] !=0:
            tmp = arr[pre]
            arr[pre] = arr[cur]
            arr[cur] = tmp
            pre +=1
            cur +=1
    return arr

def swap(head):

    if head.next:
        tmp = head.next
        head.next = swap(head.next.next)
        tmp.next = head
        return tmp
    else:
        return head

def reverse(head):
    p=None
    while head:
        tmp = head.next
        head.next = p
        p= head
        head  = tmp
    return p

def reverse2(head):

    if not head or not head.next:
        return head

    p = reverse2(head.next) #
    head.next.next = head
    head.next = None
    return p


    def merge(head1,head2):
        if not head1:
            return head2
        if not head2:
            return head1
        
        head = ListNode(-999999)
        p = head

        while head1 or head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
        while head1:
            p.next = head1
            head1 = head1.next
        while head2:
            p.next = head2
            head2 = head2.next
        return head.next

def merge2(head1,head2):
    head = ListNode(-99999)
    if head1.val < head2.val:
        head = head1
        head.next = merge(head1.next,head2)
    else:
        head=head2
        head.next = merge(head1,head2.next)
    return head


def quicksort(arr,left,right):
    if left < right:
        start = left
        end = right
        key = arr[start]

        while start<end:
            while start<end and arr[end] > key:
                end -=1
            if start<end:
                arr[start] = arr[end]
                start +=1
            while start < end and arr[start]< key:
                start +=1
            if start < end:
                arr[end] = arr[start]
                end -=1
        arr[start] = key
        quicksort(arr,left,end-1)
        quicksort(arr,end+1,right)

def maxsum(arr):
    if not arr:
        return 0
    n  =len(arr)
    dp1=[0]*n

    # 如果第一个数字用到的话
    dp1[0] =arr[0]
    for i in range(2,n-1):
        dp1[i] = max(dp1[i-2]+arr[i],dp1[i-1])

    dp2=[0]*n
    # 如果第一个数字不用的话
    for i in range(1,n):
        dp2[i] = max(dp2[i-2]+arr[i],dp2[i-1])
    return max(max(dp1),max(dp2))    




def bs____(arr,key,left,right):
    if left > right:
        return
    
    mid = (left+right)//2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return bs(arr,key,mid+1,right)
    elif arr[mid]>key:
        return bs(arr,key,left,mid-1)
def f__(arr):
    n = len(arr)

    dp=[0]*n
    minp=9999
    for i in range(1,n):
        if arr[i-1] < minp:
            minp = arr[i-1]
        dp[i] = arr[i] - minp
    return max(dp)

def maxdepth(root):

    if not root:
        return 0
    stack=[[1,root]]
    res=0
    while stack:
        depth,node = stack.pop()
        if node.right:
            stack.append([depth+1,node.right])
        if node.left:
            stack.append([depth+1,node.left])
        res = max(depth.res)
    return res


def preorder(root):
    if not root:
        return 
    stack=[]
    res=[]
    node= root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node=node.right

    return res


def inorder(root):
    if not root:
        return 
    stack=[]
    res=[]
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node =node.right
    return res

def postorder(root):
    # 根右左
    if not root:
        return 
    stack=[]
    res=[]
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.right
        node = stack.pop()
        node = node.left
    return res[::-1]


def reverse(root):
    if not root:
        return 
    tmp = root.left
    root.left = reverse(root.right)
    root.right = reverse(tmp)
    return root

def reverse2(root):
    q =[root]
    while q:
        node = q.pop(0)
        if node:
            tmp = node.left

            node.left = node.right
            node.right = tmp
            q.append(node.left)
            q.append(node.right)
    return root

def delete(head):

   p = ListNode(-9999)
   p.next = head
   pre = p
   cur = head
   while cur:
       flag = False
       while cur.next and cur.val == cur.next.val:
           flag =True
           cur =cur.next
        if flag ==True:
            pre.next = cur.next
        else:
            pre=cur
        cur = cur.next
    retur p.next

def quicksort(arr.left,right):
    if left < right:
        start = left
        end = right
        key = arr[start]

        while start < end
            while start < end and arr[end]>key:
                end = end-1
            if start<end:
                arr[start] = arr[end]
                start +=1
            while start < end and arr[start] < key:
                start = start+1
            if start < end:
                arr[end] = arr[start]
            arr[start] = key
            quicksort(arr.left.start-1)
            quicksort(arr,start+1,right)
            return arr
def mergesort(arr):
    if len(arr)<=1:
        return arr
    i  = len(arr)//2

    left = mergesort(arr[:i])
    right = mergesort(arr[i:])
    return merge(left,right)





### 面试 
arr=[1,200,10,120,30,8,88,4]
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
head =ListNode(arr[0])
def build(arr):
    for i in range(1,len(arr)):
        tmp = ListNode(arr[i])
        head.next = tmp
    return head

def f(head):
    res1= head
    res2=head.next
    head = head.next
    flag = 0
    while head:
        if head.next and flag ==0:
            res1.next = head
            head = head.next
            flag =1
        if head.next and flag == 1:
            res2.next = head
            head = head.next
            flag =0
    return res1,res2

def reverse(head):
    p = None
    
    while head:
        tmp = head.next
        head.next = p
        
        p = head
        head = tmp
    return p

def merge(head1,head2):
    
    head = ListNode(-9999)
    
    p = head
    
    while head1 and head2:
        if head1.val < head2.val :
            p.next =head1
            head1 = head1.next
            p = p.next
        else:
            p.next = head2
            p = p.next
            head2 = head2.next
    if head1:
        p.next = head1
    else:
        p.next = head2
    return head.next
print(build(arr))
#res1,res2=f(head)
#res2 = reverse(res2)
#res = merge(res1,res2)
    
            
         
        