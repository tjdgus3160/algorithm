# 11502번
from itertools import product
import sys
input=sys.stdin.readline

l=[True for _ in range(1001)]
l[1]=False
for i in range(2,int(1001**0.5)+1):
    if l[i]:
        j=i+i
        while j<=1000:
            l[j]=False
            j+=i

for _ in range(int(input())):
    k=int(input())
    tmp=[]
    for i in range(2,k):
        if l[i]:
            tmp.append(i)
    for sub in product(tmp,repeat=3):
        if sum(sub)==k:
            print(*sub)
            break
    else:
        print(0)