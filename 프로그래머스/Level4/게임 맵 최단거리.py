from collections import deque
import sys
INF=sys.maxsize

def solution(arr):
    res = INF
    n=len(arr)
    m=len(arr[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq=deque()
    dq.append([1,0,0])
    arr[0][0]=0
    while dq and res==INF:
        k,x,y=dq.popleft()
        if x == m - 1 and y == n - 1:
            return k
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx]:
                dq.append([k+1,nx,ny])
                arr[ny][nx] = 0
        # print(dq)
    return -1