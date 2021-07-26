def solution(n, t, m, arr):
    arr=sorted([h*60+m for h,m in [[*map(int,i.split(':'))] for i in arr]])
    res=arr[0]-1
    loc=0
    for i in range(n):
        time=9*60+i*t
        k=0
        while k<m and loc<len(arr) and arr[loc]<=time:
            k+=1
            loc+=1
        if i==n-1:
            if k<m:
                res=time
            else:
                res=arr[loc-1]-1
    return str(res//60).rjust(2,'0')+":"+str(res%60).rjust(2,'0')

n=2 # 횟수
t=1 # 간격
m=2 # 최대인원
arr=["09:00", "09:00", "09:00", "09:00"]
print(solution(n,t,m,arr))
