"""

49.字母异位词

"""


def groupAnagrams(strs):
    if not strs:
        return

    tmp={}
    for i,astr in enumerate(strs):
        s = "".join(sorted(astr))

        if tmp.get(s) :
            tmp[s].append(astr)
        else:
            tmp[s] = [astr]



    return list(tmp.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


# 我的蹩脚code
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    if not strs:
        return

    tmp = {}
    for i, astr in enumerate(strs):
        s = str(sorted(astr))

        if tmp.get(s):
            tmp[s].append(i)
        else:
            tmp[s] = [i]

    res = []

    for k, v in tmp.items():
        tmp2 = []
        for j in v:
            tmp2.append(strs[j])
        res.append(tmp2)
    return res

