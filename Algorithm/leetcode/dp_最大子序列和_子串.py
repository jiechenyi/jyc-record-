"""
[1,3,1,-1,9,-5,4,-7,8]


"""
class MaxSum(object):

    """
    子串(连续的子列)
    """
    def f1(self,arr):
        if not arr:
            return 0
        n = len(arr)

        dp = [0] *n # 记录到当前位置位置为止的最大和
        dp[0] = arr[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+arr[i],arr[i])
        return max(dp)



