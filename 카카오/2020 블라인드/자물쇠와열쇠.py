# hint: lock을 확장시킨후 key와 비교, key를 회전시키는 함수 구현

import copy
def trans(key,n):
    tra=[]
    for i in range(n):
        tmp=[]
        for j in range(n-1,-1,-1):
            tmp.append(key[j][i])
        tra.append(tmp)
    return tra

def check(lock,n,m):
    for i in range(n-1,m+n-1):
        for j in range(n-1,m+n-1):
            if lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n=len(key)
    m=len(lock)
    for i in range(2*n-2+m):
        if i<n-1:
            lock.insert(0,[0]*(2*n-2+m))
        elif i>=n-1+m:
            lock.append([0]*(2*n-2+m))
        else:
            lock[i]=[0]*(n-1)+lock[i]+[0]*(n-1)

    for _ in range(4):
        for i in range(len(lock)-n+1):
            for j in range(len(lock)-n+1):
                tmp =copy.deepcopy(lock)
                flag=True
                for k in range(n):
                    for l in range(n):
                        if tmp[i+k][j+l]!=1:
                            tmp[i+k][j+l]=key[k][l]
                        else:
                            if key[k][l]==1:
                                tmp[i + k][j + l]+=1
                                flag=False
                                break
                    if not flag:
                        break
                if check(tmp,n,m):
                    return True
        key=trans(key,n)
    return False

key=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lock=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(solution(key,lock))
#tmp=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
#print(check(tmp,3,3))
