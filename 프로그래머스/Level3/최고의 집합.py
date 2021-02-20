def solution(n, s):
    a,b=divmod(s,n)
    if a<1:
        return [-1]
    res=[a]*n
    for i in range(n-1,-1,-1):
        if b>0:
            res[i]+=1
            b-=1
        else:
            break
    return res