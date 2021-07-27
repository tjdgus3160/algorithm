def solution(arr):
    res=0
    for i in range(len(arr)-1):
        left=arr[i]
        right=arr[i+1]
        l,r=i,i+1
        k=-1
        while 0<=l and r<len(arr):
            if k==0:
                left+=arr[l]
            elif k==1:
                right+=arr[r]
            if left==right:
                res=max(res,left)
                l-=1
                k=0
            elif left>right:
                r+=1
                k=1
            else:
                l-=1
                k=0
    return res

arr=[1,1,2,3]
print(solution(arr))