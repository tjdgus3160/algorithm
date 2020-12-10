# 수가 적을때는 일일이 탐색, 투입친구수를 1부터 증가하면서 탐색, 선택한 친구들 배치 순열 사용, 원형임으로 deque의 rotate사용

from collections import deque
import itertools

def next_index(queue,d,start_index):
    start_num=queue[start_index]
    for i in range(1,d+1):
        try:
            if queue[start_index+1]==start_num+i:
                start_index+=1
        except:
            break
    return start_index+1

def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak=deque(weak)

    for i in range(1,len(dist)+1):   # 투입 친구수
        if i==1:
            d=dist[0]
            for _ in range(len(weak)):
                if weak[-1] <= weak[0]+d:
                    return 1
                weak.rotate(-1)
                weak[-1]+=n
            weak=deque(map(lambda x:x%n,weak))
        else:
            dist_2=list(itertools.permutations(dist[:i]))
            for select_set in dist_2:
                for _ in range(len(weak)):
                    start_index=0
                    for d in select_set:
                        start_index=next_index(weak,d,start_index)
                        if start_index==len(weak):
                            return i
                    weak.rotate(-1)
                    weak[-1]+=n
                weak=deque(map(lambda x:x%n,weak))
    return -1

n=12
weak=[1, 5, 6, 10]
dist=[1, 2, 3, 4]
print(solution(n,weak,dist))
