def solution(n):
    res=0
    cur=1
    start=1
    end=1
    while start<=end:
        if cur<n:
            end+=1
            cur+=end
        else:
            if cur==n:
                res += 1
            cur-=start
            start+=1
    return res