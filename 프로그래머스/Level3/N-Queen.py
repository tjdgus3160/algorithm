isused1 = [False] * 40
isused2 = [False] * 40
isused3 = [False] * 40

res=0

def func(k,n):
    global res
    if k==n:
        res+=1
        return
    for i in range(n):
        if isused1[i] or isused2[i+k] or isused3[k-i+n-1]:
            continue
        isused1[i]=True
        isused2[k + i]=True
        isused3[k-i+n-1]=True
        func(k+1,n)
        isused1[i]=False
        isused2[k + i]=False
        isused3[k-i+n-1]=False

def solution(n):
    global res
    func(0,n)
    return res