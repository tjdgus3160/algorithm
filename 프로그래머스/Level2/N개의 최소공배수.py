from math import gcd

def solution(arr):
    res=0
    for i in arr:
        if res==0:
            res=i
        else:
            res=res*i//gcd(res,i)
    return res