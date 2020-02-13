"""
56.合并区间
给出一个区间的集合，请合并所有重叠的区间。

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

"""
# 不使用额外的空间
def merge(intervals):
    if not intervals:
        return []
    if len(intervals) ==1:
        return intervals
    i=1
    flag=0
    intervals.sort()
    while intervals:
        if i < len(intervals):
            arr1 = intervals[i-1]
            arr2 = intervals[i]
            newarr =[]
            if arr1[1] >= arr2[0]:
                newarr=[arr1[0], max(arr1[1],arr2[1])]

            if newarr != []:
                intervals[i-1]= newarr
                intervals.pop(i)
                flag =0
                i=1
            else:
                flag +=1
                i+=1

        if flag == len(intervals)-1:
            break

    return intervals

intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(merge(intervals))



# 利用额外的array来存储结果
#
def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1]< interval[0]:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

