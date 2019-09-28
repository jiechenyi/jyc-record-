"""

165.比较版本号

"""


def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    if not version1 or not version2:
        return
    a = list(map(int, version1.split(".")))
    b = list(map(int, version2.split(".")))
    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0
    flag = 0
    while i < n1 and j < n2:
        if a[i] < b[j] and flag == 0:
            flag = -1
        elif a[i] > b[j] and flag == 0:
            flag = 1
        i += 1
        j += 1
    if i < n1 and sum(a[i:]) != 0 and flag == 0:
        return 1
    if j < n2 and sum(b[j:]) != 0 and flag == 0:
        return -1
    return flag


a = "0.1"
b = "0.0.1"

print(compareVersion(a,b))