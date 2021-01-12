# 10828번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    cmd=input().rstrip('\n')
    if "push" in cmd:
        s,v=cmd.split()
        arr.append(v)
    elif "pop" in cmd:
        print(arr.pop() if arr else -1)
    elif "size" in cmd:
        print(len(arr))
    elif "empty" in cmd:
        print(1 if not arr else 0)
    else:
        print(arr[-1] if arr else -1)