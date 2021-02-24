def func(k,cur,n):
    global res
    if k==n:
        res+=1
        return
    tmp.append('(')
    func(k+1,cur+1,n)
    tmp.pop()
    if cur:
        tmp.append(')')
        func(k,cur-1,n)
        tmp.pop()

res=0
tmp=['(']
def solution(n):
    global res
    func(1,1,n)
    return res