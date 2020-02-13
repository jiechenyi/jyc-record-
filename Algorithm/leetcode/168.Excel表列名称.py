"""
168.Excel表列名称
给定一个正整数，返回它在 Excel 表中相对应的列名称
"""

def convertToTitle(n):

    if (n-1)//26==0:
        return chr(65+(n-1)%26)

    else:
        return convertToTitle((n-1)//26) + chr(65+(n-1)%26)

n = 52

print(convertToTitle(n))