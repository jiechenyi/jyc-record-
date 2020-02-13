"""
100.相同的树

判断两个二叉树是否相同


"""
# 递归
def isSameTree(p,q):
    if p and q:
        if p.val == q.val:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    elif not p and not q:
        return True
    else:
        return False

def isSameTree(p,q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.right,q.right) and \
        isSameTree(p.left, q.left)

# 迭代 利用栈

def isSameTree(p,q):

    que = [(p,q)]

    while que:
        p,q = que.pop(0)

        if check(p,q) == False:
            return False

        if p :
            que.append((p.left, q.left))
            que.append((p.right,q.right))
    return True



def check(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val == q.val:
        return True
    else:
        return False

