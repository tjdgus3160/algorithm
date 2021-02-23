def solution(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                arr[i][j]+=arr[i-1][j]
            elif j==i:
                arr[i][j]+=arr[i-1][j-1]
            else:
                arr[i][j]+=max(arr[i-1][j-1],arr[i-1][j])
    return max(arr[-1])