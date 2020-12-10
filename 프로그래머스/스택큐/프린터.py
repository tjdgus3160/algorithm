from collections import deque
def solution(arr, x):
    answer = 0
    dq = deque([(v,i) for i,v in enumerate(arr)])
    while True:
        t = dq.popleft()
        if dq and max(dq)[0]>t[0]:
            dq.append(t)
        else:
            answer+=1
            if t[1]==x:
                break
    return answer

arr=[1,1,9,1,1,1]
x=0
print(solution(arr,x))

## any사용
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer