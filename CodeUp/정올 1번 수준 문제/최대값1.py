from collections import Counter
import operator
import sys
input=sys.stdin.readline

tmp=[]
for i in range(9):
    tmp.append(int(input()))
print(max(tmp))
print(tmp.index(max(tmp))+1)

