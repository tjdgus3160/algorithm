# 16922번
from itertools import combinations_with_replacement
import sys
input=sys.stdin.readline

arr=[1,5,10,50]
dic={}
n=int(input())
for sub in combinations_with_replacement(arr,n):
    k=sum(sub)
    dic[k]=True
print(len(dic))