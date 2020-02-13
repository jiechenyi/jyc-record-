"""
93.复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

合法的ip是由四个数组成 每个数在0～255  之间
"""
# dfs 回溯
def restoreIpAddresses(s):

    res = []

    cur = []

    def dfs(s, start, cur):
        if start == len(s): # 搜索到了尽头
            if len(cur) == 4: # cur 中如果有四个数字的话 将其组合起来变成一个ip
                tmp = ""
                for i in range(len(cur)):
                    tmp += cur[i]
                    if i != len(cur) - 1:
                        tmp += "."
                res.append(tmp)

        else:
            if len(cur) > 4: #如果cur中数字大于4个 直接return
                return
            for i in range(start, len(s)):
                if i < start + 3: # 只需从start开始往后再寻找2个字符
                    ss = s[start:i + 1]# 将 start ～ i 的字符拿出来
                    if ss[0] == "0" and len(ss) > 1: # 0开头的 长度超过1 的字符肯定不合法
                        break
                    num = int(ss)
                    if num >= 0 and num <= 255: # 合法字符将其加入 cur
                        cur.append(ss)

                        dfs(s, i + 1, cur) # start 改为 i+1
                        cur.pop()

                    else:
                        break

    dfs(s,0,cur)
    return res

def dfs(s,start,cur):
    if start == len(s):
        if len(cur)==4:
            tmp =[]
            for i in range(len(cur)):
                tmp.append(cur[i])
                if i!=  len(cur)-1:
                    tmp.append(".")
            res.append(tmp)
        return
    else:
        if len(cur)>=4:
            return
        for i in range(start,len(s)):
            if i< start+3 :
                ss = s[start,i+1]
                if ss[0] == "0" and  len(ss)>1:
                    break
                num = int(ss)
                if num>=0 and num<=255:
                    cur.append(ss)

                    dfs(s,i+1,cur)
                    cur.pop()

                else:
                    break



