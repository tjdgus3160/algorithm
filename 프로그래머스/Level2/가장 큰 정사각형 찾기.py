def solution(arr):
    res=0
    r=len(arr)
    c=len(arr[0])
    dp=[[0 for _ in range(c+1)]for _ in range(r+1)]
    for i in range(1,r+1):
        for j in range(1,c+1):
            if arr[i-1][j-1]:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                res=max(res,dp[i][j])
    return res*res