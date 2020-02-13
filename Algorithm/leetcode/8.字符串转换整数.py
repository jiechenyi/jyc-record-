def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+"]

    str = str.strip()
    if not str or str[0] not in numlist:
        return 0

    tmp = ''
    for i in str:
        if tmp == '':
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9",'0','+','-']:
                tmp += i

            else:
                continue
        else:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9",'0']:
                tmp += i


            else:
                break
    if tmp == '-' or tmp == '+' or tmp == '':
        return 0
    print(tmp)
    tmp2 =''
    tmp2 += tmp[0]
    j=1
    while j < len(tmp):
        if (tmp2 =='+' or tmp2 == '-') and tmp[j] =='0':
            j +=1

        elif tmp2 =='0':
            tmp2='+'
        else:
            tmp2 += tmp[j]
            j+=1
    print(tmp2)
    if tmp2 == '-' or tmp2 == '+' or tmp2 == '':
        return 0

    res = eval(tmp2)
    if res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if res < -2 ** 31:
        return -2 ** 31
    return res

str ="010"
print(myAtoi(str))

# 用正则表达式解
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
