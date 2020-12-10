from collections import Counter
import operator
import sys
input=sys.stdin.readline

tmp=[]
for i in range(10):
    tmp.append(int(input()))
tmp.sort()
print(sum(tmp)//10)
c=Counter(tmp)
print(sorted(c.items(),key=operator.itemgetter(1),reverse=True)[0][0])
