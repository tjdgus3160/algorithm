import heapq
def solution(arr, k):
    answer = 0
    heapq.heapify(arr)
    while True:
        if len(arr)==1 and arr[-1]<k:
            answer=-1
            break
        if arr[0]>=k:
            break
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        heapq.heappush(arr,a+b*2)
        answer+=1
    return answer

arr=[0,0,0,2]
k=2
print(solution(arr,k))