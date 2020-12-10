# hint: 힙 2개 만들어서 현재 시간 기준 처리할 일 힙에 넣고 그리디
import heapq
def solution(jobs):
    answer = []
    tmp=[]
    heapq.heapify(jobs)
    time = jobs[0][0]
    for i in jobs:
        if i[0]<=time:
            a,b=heapq.heappop(jobs)
            heapq.heappush(tmp,(b,a))
    while tmp:
        t=heapq.heappop(tmp)
        time=max(t[0]+time,t[1]+t[0])
        answer.append(time-t[1])
        while jobs and jobs[0][0]<=time:
            a,b=heapq.heappop(jobs)
            heapq.heappush(tmp,(b,a))
        if not tmp and jobs:
            a, b = heapq.heappop(jobs)
            heapq.heappush(tmp, (b, a))
    return sum(answer)//len(answer)

j=[[0, 3], [1, 9], [2, 6], [30, 3]]
print(solution(j))