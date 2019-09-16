"""

全排列（递归）

"""

# 全排列
# 递归

arr=[1,2,3]
def printArray(arr,n):
    for i in range(n):
        print(arr[i])
    print("\n")
def savetolist(res,arr):
    res.append(arr)

def permutation(arr,l,r,res):

    if l == r:
        savetolist(res,arr)
    else:
        for i in range(l,r+1,1):
            # // swap(arr,0,i)
            tmp = arr[l]
            arr[l] = arr[i]
            arr[i] = tmp
            permutation(arr,l+1,r,res)
            # swap(arr,0,i)
            tmp = arr[l]
            arr[l] = arr[i]
            arr[i] = tmp
def main(arr):
    res=[]
    permutation(arr,0,len(arr)-1,res)
    print(res)

main(arr)

