res=[0,0]
def check(x,y,k,arr):
    if k==1:
        res[arr[y][x]]+=1
        return
    cur=arr[y][x]
    for i in range(y,y+k):
        for j in range(x,x+k):
            if arr[i][j]!=cur:
                check(x, y, k // 2, arr)
                check(x + k // 2, y, k // 2, arr)
                check(x, y + k // 2, k // 2, arr)
                check(x + k // 2, y + k // 2, k // 2, arr)
                return
    res[cur] += 1

def solution(arr):
    global res
    check(0,0,len(arr),arr)
    return res