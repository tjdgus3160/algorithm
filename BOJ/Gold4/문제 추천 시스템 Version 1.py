# 21939번
from heapq import heappush,heappop,heapify
import sys
input=sys.stdin.readline

easy=[]
hard=[]
clear=set()
dic={}
for _ in range(int(input())):
    p,l=map(int,input().split())
    dic[p]=l
    heappush(easy,[l,p])
    heappush(hard,[-l,-p])

for _ in range(int(input())):
    cmd,*tmp=input().rstrip().split(' ')
    if cmd=='add':
        p,l=map(int,tmp)
        dic[p]=l
        heappush(easy, [l,p])
        heappush(hard, [-l,-p])
    elif cmd=='solved':
        clear.add(int(tmp[0]))
    elif int(tmp[0])==1:
        while -hard[0][1] in clear or -hard[0][0]!=dic[-hard[0][1]]:
            heappop(hard)
        print(-hard[0][1])
    else:
        while easy[0][1] in clear or easy[0][0]!=dic[easy[0][1]]:
            heappop(easy)
        print(easy[0][1])