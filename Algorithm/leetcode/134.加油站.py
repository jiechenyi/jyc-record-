# _*_coding:utf-8 _* _
"""
134.加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。


"""

def canCompleteCircuit(gas, cost):

    if sum(gas)-sum(cost) <0:
        return -1
    start = None

    for i in range(len(gas)):
        if gas[i] < cost[i]:
            continue
        else:
            start = i

            break
    if start == None :
        return -1
    n = len(gas)
    cur_tank = gas[start]

    i = start
    while cur_tank>=0 :

        if cur_tank  >= cost[i]:
            if i == n-1 :
                i = -1
            cur_tank = cur_tank - cost[i] + gas[i+1]

        else :
            cur_tank = -1
        i = i +1
        if cur_tank < 0:
            cur_tank = gas[i]
            start = i
        elif start == i:
            return start
    return -1

gas=[5,1,2,3,4]
cost = [4,4,1,5,1]
print(canCompleteCircuit(gas, cost))



