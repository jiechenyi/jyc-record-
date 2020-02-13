"""
131.分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。
"""


def partition(s):

    if not s:
        return []
    res=[]
    cur =[]

    def helper(s, start, cur):
        if start == len(s):
            res.append(cur[:])
            return

        else:
            j = 1
            while start+ j <= len(s):
                ss =s[start:start+j]
                if ss[::-1] == ss[:]:
                    cur.append(ss[:])
                    helper(s, start+j,cur)
                    cur.pop()

                j += 1


    helper(s, 0, cur)
    return res

s = 'efe'
print(partition(s))
