from _collections import deque
import sys
input=sys.stdin.readline

def bfs(a,b,c,d):
    if c==0 and d==0:
        return 0
    q=deque([(0,0)])
    s=set()
    res=0
    while q:
        k=len(q)
        for _ in range(k):
            x,y=q.popleft()
            if x==c and y==d:
                return res
            if (x,y) in s:
                continue
            s.add((x,y))
            if x==0:
                q.append((a,y))
            else:
                q.append((0,y))
            if y==0:
                q.append((x,b))
            else:
                q.append((x,0))
            if x>0 and y<b:
                if x+y<=b:
                    q.append((0,x+y))
                else:
                    q.append((x-(b-y),b))
            if y>0 and x<a:
                if x+y<=a:
                    q.append((x+y,0))
                else:
                    q.append((a,y-(a-x)))
        #print(q)
        res+=1
    return -1

a,b,c,d=map(int,input().split())
print(bfs(a,b,c,d))