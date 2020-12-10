# hint: 가능한 조합에서 중복이 발생하지 않는 경우 최소성을 만족하는지 확인, 문자열 in 은 덩어리를 하나로 인식함->set으로 판별

import itertools
def solution(arr):
    key=[]
    n=len(arr[0])   # 속성 수
    m=len(arr)      # 튜플수
    tmp=[]
    for i in range(1,n+1):
        tmp+=[*map(list,itertools.combinations(range(n),i))]
    for i in tmp:
        cand = "".join(map(str, i))
        flag = 1
        for p in key:
            if len(set(list(p))-set(list(cand)))==0:
                flag = 0
                break
        if flag:
            q = [""]*m
            for j in i:
                for k in range(m):
                    q[k]+=("-"+arr[k][j])
            if len(set(q)) == m:
                key +=[cand]
    return len(key)

arr=[["b","2","a","a","b"],["b","2","7","1","b"],["1","0","a","a","8"],["7","5","a","a","9"],["3","0","a","f","9"]]
print(solution(arr))
