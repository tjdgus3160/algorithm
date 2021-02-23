def solution(m, n, puddles):
    arr=[[0]*m for _ in range(n)]
    for x,y in puddles:
        arr[y-1][x-1]=-1
    for i in range(m):
        if arr[0][i] != -1:
            arr[0][i]=1
        else:
            break
    for i in range(n):
        if arr[i][0] != -1:
            arr[i][0]=1
        else:
            break
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j]==0:
                if arr[i-1][j]!= -1:
                    arr[i][j]+=arr[i-1][j]
                if arr[i][j-1]!= -1:
                    arr[i][j]+=arr[i][j-1]
    return arr[n-1][m-1]%1000000007