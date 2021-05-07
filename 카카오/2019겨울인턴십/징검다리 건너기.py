def func(arr,v,k):
    cnt=0
    for i in arr:
        if i<=v:
            cnt+=1
        else:
            cnt=0
        if cnt==k:
            return False
    return True

def solution(stones, k):
    res = 0
    start=1
    end=max(stones)
    while start<=end:
        mid=(start+end)//2
        if func(stones,mid,k):
            start=mid+1
        else:
            res=mid
            end=mid-1
    return res