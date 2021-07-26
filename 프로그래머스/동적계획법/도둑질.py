def check(arr):
    n=len(arr)
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[:2])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
    return dp[-1]

def solution(arr):
    if len(arr)<3:
        return max(arr)
    return max(check(arr[1:]),check(arr[:-1]))