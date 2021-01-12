# 10845번
import sys
input=sys.stdin.readline

q=[]

for _ in range(int(input())):
    cmd=input().rstrip('\n')
    if "push" in cmd:
        s,v=cmd.split()
        q.append(v)
    elif "pop" in cmd:
        print(q.pop(0) if q else -1)
    elif "size" in cmd:
        print(len(q))
    elif "empty" in cmd:
        print(1 if not q else 0)
    elif "front" in cmd:
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)