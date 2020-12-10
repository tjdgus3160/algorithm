# hint: 트럭이 진입못할시 큐에 0을 넣어서 지나가는 흐름 만들기
import queue
def solution(l, w, arr):
    answer=0
    q = queue.Queue(maxsize=l)
    cw=0
    for i in arr:
        while True:
            if q.full():
                cw-=q.get()
            if w-cw>=i:
                cw+=i
                q.put(i)
                answer+=1
                break
            else:
                q.put(0)
                answer+=1
    return answer+l

l=5 # 다리 길이
w=5 # 다리 허용 무게
arr=[2, 2, 2, 2, 1, 1, 1, 1, 1] # 트럭의 중량
print(solution(l,w,arr))