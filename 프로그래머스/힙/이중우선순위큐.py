# bisect 살짝 더 빠름

import bisect
def solution(arr):
    answer = []
    for i in arr:
        c,v=i.split()
        v=int(v)
        if c =='I':
            answer.insert(bisect.bisect(answer,v),v)
        else:
            if answer and v==-1 :
                del answer[0]
            elif answer and v==1:
                answer.pop()
    return [answer[-1],answer[0]] if answer else [0,0]

arr=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(arr))

# heapq
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]
