"""
乘积最大的连续子序列

"""

class MaxMultiply(object):
    def f1(self,arr):
        if not arr:
            return 
        n = len(arr)
        minp=arr[:]
        maxp =arr[:]
        for i in range(1,n):
            minp[i] = min(minp[i-1]*arr[i],maxp[i-1]*arr[i],arr[i])
            maxp[i] = max(maxp[i-1]*arr[i],minp[i-1]*arr[i],arr[i])

        return max(maxp)


