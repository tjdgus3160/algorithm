def solution(enter, leave):
    n=len(enter)
    res=[0]*n
    s=set()
    start=0
    for l in leave:
        while l not in s:
            s.add(enter[start])
            start+=1
        s.remove(l)
        for p in s:
            res[p-1]+=1
        res[l-1]+=len(s)
    return res