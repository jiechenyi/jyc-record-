"""
2019.06.26
反转字符串
不使用额外的数组空间
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return 
        m = len(s)/2
        for i in range(m):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp
        return s