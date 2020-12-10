# 1018번
import sys
input=sys.stdin.readline

def diff(s1,s2):
    res=0
    for i in range(8):
        if s1[i]!=s2[i]:
            res+=1
    return res

arr=[]
n,m=map(int,input().split())
for _ in range(n):
    arr.append(input()[:-1])
res=100
a="WBWBWBWB"
b="BWBWBWBW"
for i in range(n-7):
    for j in range(m-7):
        tmpa=0
        tmpb=0
        for k in range(i,i+8):
            comp=arr[k][j:j+8]
            if k%2==0:
                tmpa+=diff(a,comp)
                tmpb+=diff(b,comp)
            else:
                tmpa += diff(b, comp)
                tmpb += diff(a, comp)
        res=min(res,tmpa,tmpb)
print(res)