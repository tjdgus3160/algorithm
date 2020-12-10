from collections import deque
n=int(input())
max=2**64-1
q=deque()
q.appendleft(1)
while True:
    tmp=q.popleft()
    if tmp>max:
        print(0)
        break
    if tmp%n==0:
        print(tmp)
        break
    q.append(tmp*10)
    q.append(tmp*10+1)
