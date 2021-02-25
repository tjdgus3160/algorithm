def solution(name):
    arr=[min(ord(i)-ord('A'),ord('Z')+1-ord(i)) for i in name]
    k=0
    res=0
    while True:
        res += arr[k]
        arr[k] = 0
        print(k)
        print(arr)
        if sum(arr) ==0:
            break
        left,right=1,1
        while arr[k-left] == 0:
            left+=1
        while arr[k+right] == 0:
            right+=1
        if left<right:
            res+=left
            k-=left
        else:
            res+=right
            k+=right
    return res

# 문제가 있는 코드
# 반례 "ABBBBAAAAAAAAABBB" 17인데 18나옴 다른 모든 코드도 18로 통과