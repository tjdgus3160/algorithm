def solution(n):
    res=0
    while n>1:
        if n%2==0:
            n//=2
        else:
            n-=1
            res+=1
    return res+1