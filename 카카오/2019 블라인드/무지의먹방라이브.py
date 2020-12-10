# hint: 필요 시간 정렬, 작은거 부터 한번에 시간 지우기, 나머지 시간으로 나머지 연산써서 다음 순서 구하기

from collections import deque
def solution(arr, k):
    dq=deque(sorted([[arr[i],i+1] for i in range(len(arr))]))
    time=0
    prev=0
    while time<=k:
        if not dq:
            return -1
        if time+(dq[0][0]-prev)*len(dq)>k:
            break
        time += (dq[0][0] - prev) * len(dq)
        t=dq.popleft()
        prev=t[0]
    if dq:
        tmp=sorted(dq,key=lambda x:x[1])
        return tmp[((k-time)%(len(tmp)))][1]
    return -1

arr=[10, 10, 10]
k=27
print(solution(arr,k))