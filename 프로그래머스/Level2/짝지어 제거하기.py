from collections import deque
def solution(s):
    dq=deque()
    for i in s:
        if dq and dq[-1]==i:
            dq.pop()
        else:
            dq.append(i)
    if dq:
        return 0
    return 1