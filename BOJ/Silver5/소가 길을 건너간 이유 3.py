# 14469번
from queue import PriorityQueue
import sys
input=sys.stdin.readline

q=PriorityQueue()
for _ in range(int(input())):
    q.put([*map(int,input().split())])
res=None
while not q.empty():
    a,b=q.get()
    if res==None or res<=a:
        res=a+b
    elif res>a:
        res+=b
print(res)
