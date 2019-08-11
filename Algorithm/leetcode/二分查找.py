# 感觉还蛮容易错的...
class BinarySearch(object):
    """
    递归
    """
    def bs1(self,arr,key,left,right):
        if left > right:
            return -1
        
        mid = (left+right)//2
        
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            return self.bs1(arr,key,mid+1,right)
        elif arr[mid] > key:
            return self.bs1(arr,key,left,mid-1)
    """
    非递归
    """
    def bs2(self,arr,key):
        left = 0
        right = len(arr)
        while left <=right:

            mid = (left+right)//2
            if arr[mid] == key:
                return mid
            if arr[mid] > key:
                right = mid-1
            if arr[mid] < key:
               left = mid+1
        return 
            

a = BinarySearch()
print(a.bs2([1,2,3,4,5,6],5))
        