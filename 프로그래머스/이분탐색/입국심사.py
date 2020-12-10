# 1~최대 걸릴수 있는 시간사이에서 만족하는 최소 시간 구하기

def solution(n, times):
    answer=0
    start=1
    end=max(times)*n
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for i in times:
            cnt+=mid//i
            if cnt>=n:
                break
        if cnt>=n:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer

n=1000000000
arr= [1, 1000000000, 1000000000]
print(solution(n,arr))