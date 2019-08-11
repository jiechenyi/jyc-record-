

class sort(object):

    """
    冒泡
    """

    def bubblesort(self,arr):
        n =len(arr)
        for i in range(n):
            for j in range(1,n-i):
                if arr[j] < arr[j-1]:
                    tmp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = tmp
                    
        print(arr)
    """
    快排
    """
    def quicksort(self,arr,left,right):
        if left>=right:
            return
        start = left
        end = right
        key = arr[left]

        while start < end:
            while start<end and arr[end]>=key:
                end = end -1
            if start <end:
                arr[start] = arr[end]
                start +=1
            while start<end and arr[start] <key:
                start += 1
            if start <end :
                arr[end] = arr[start]
                end = end-1
        arr[start]= key
        self.quicksort(arr,left,start-1)
        self.quicksort(arr,start+1,right)
        return arr
    """
    选择排序

    """
    def selectsort(self,arr):
        n = len(arr)
        for i in range(n):
            min = i
            for j in range(i,n):
                if arr[j] < arr[min]:
                    min = j
            if min != i:
                tmp = arr[i]
                arr[i] = arr[min]
                arr[min] = tmp
        return arr
    """
    直接插入排序

    """
    def insertsort(self,arr):
        n = len(arr)
        for i in range(1,n):
            for j in range(i,0,-1):
                if arr[j]< arr[j-1]:
                    tmp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = tmp
        return arr

    """
    归并
    """
    @ staticmethod
    def merge(arr1,arr2):
        res  = []
        
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                res.append(arr1[0])
                arr1.pop(0)
            else:
                res.append(arr2[0])
                arr2.pop(0)
        if arr1:
            res.extend(arr1)
        if arr2:
            res.extend(arr2)
        return res
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        i = len(arr)//2
        left = self.mergesort(arr[:i])

        right = self.mergesort(arr[i:])
        return self.merge(left,right)
a= sort()
print(a.mergesort([2,4,5,3,1]))
                

