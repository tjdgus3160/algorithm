# hint: 1~도착거리에서 사이거리를 이진탐색, 돌 간 거리가 사이거리보다 작은 돌들이 n개 있어야함
def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start=1
    end=distance
    while start<=end:
        mid=(start+end)//2
        prev=0
        k=0
        for i in rocks:
            if i-prev<mid:
                k+=1
                if k>n:
                    break
            else:
                prev=i
        if k<=n:
            start=mid+1
            answer=mid
        else:
            end=mid-1
    return answer

d=25
arr=[2,14,11,21,17]
n=1
print(solution(d,arr,n))
