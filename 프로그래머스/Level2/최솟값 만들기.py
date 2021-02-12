def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    res=0
    for sub in zip(A,B):
        res+=sub[0]*sub[1]
    return res