import bisect

def solution(A, B):
    n=len(A)
    B.sort()
    res=0
    cnt=n
    for i in range(n):
        loc=bisect.bisect_right(B, A[i])
        if loc<cnt:
            res+=1
            cnt-=1
            del B[loc]
    return res