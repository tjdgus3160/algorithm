def solution(arr):
    r=len(arr)
    c=len(arr[0])
    dp=[[0 for _ in range(c)]for _ in range(r)]
    dp[0]=arr[0]
    for i in range(1,r):
        for j in range(c):
            k=max([dp[i-1][t] for t in range(c) if t!=j])
            dp[i][j]=arr[i][j]+k
    return max(dp[r-1])