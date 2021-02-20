from itertools import permutations
from math import factorial

def solution(n, k):
    arr=[*range(1,n+1)]
    res=[]
    while n>1:
        f=factorial(n-1)
        if k<f:
            res.append(arr[0])
            del arr[0]
        else:
            a,b=divmod(k,f)
            if b==0:
                for idx, sub in enumerate(permutations(arr, n)):
                    if idx + 1 == k:
                        res += list(sub)
                        n = 0
                        break
            else:
                res.append(arr[k//f])
                del arr[k//f]
                k%=f
        n-=1
    return res