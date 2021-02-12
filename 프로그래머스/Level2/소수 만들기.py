from itertools import combinations

def solution(nums):
    res=0
    prim=[True]*(3001)
    for i in range(2,int(3000**0.5)+1):
        if prim[i]:
            j=i+i
            while j<=3000:
                prim[j]=False
                j+=i
    for sub in combinations(nums,3):
        k=sum(sub)
        if prim[k]:
            res+=1
    return res