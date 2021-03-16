# 6236번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
start=max(arr) # 최소한으로 금액의 최대값은 가져야한다.
end=sum(arr) # 최댓값으로 모든 금액의 합(1번만 인출 할 수도 있다)
while start<end:
    mid=(start+end)//2
    cnt,cur=1,mid
    for i in arr:
        if cur<i:
            cur=mid
            cnt+=1
        cur-=i
    if cnt>m: # 조건을 만족못할경우 start를 이동
        start=mid+1
    else: # 최솟값을 구해야함으로 맞을경우 end를 이동
        end=mid-1
print(start)