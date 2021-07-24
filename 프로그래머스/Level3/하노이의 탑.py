res=[]
def func(n,a,b):
    global res
    if n==1:
        res.append([a,b])
        return
    func(n-1,a,6-a-b)
    res.append([a,b])
    func(n-1,6-a-b,b)

def solution(n):
    global res
    func(n,1,3)
    return res