import heapq

def solution(n, works):
    s=sum(works)-n
    if s<0:
        return 0
    works.sort()
    works=[-1*i for i in works]
    heapq.heapify(works)
    while n:
        k=heapq.heappop(works)
        heapq.heappush(works,k+1)
        n-=1
    return sum([pow(i,2) for i in works])

works=[2, 15, 22, 55, 55]
n=99
print(solution(n,works))