"""
125.验证回文串


"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    ss = ''
    for i in s:
        if i.isalnum():
            ss += i

    ss = ss.lower()
    print(ss)
    if ss == ss[::-1]:
        return True
    else:
        return False

s= "A man, a plan, a canal: Panama"
print(isPalindrome(s))
