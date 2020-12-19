# 13335번
import sys
input=sys.stdin.readline

n,w,l=map(int,input().split())
arr=[*map(int,input().split())]
sum,cnt=0,0
q=[]
for i in arr:
    while True:
        if not q:
            q.append(i)
            cnt+=1
            sum+=i
            break
        elif len(q)==w:
            sum-=q[0]
            q.pop(0)
        else:
            if sum+i>l:
                q.append(0)
                cnt+=1
            else:
                q.append(i)
                cnt+=1
                sum+=i
                break
print(cnt+w)