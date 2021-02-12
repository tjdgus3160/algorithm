def solution(s):
    res=[]
    for i in s:
        if i=='(':
            res.append(i)
        else:
            if res:
                res.pop()
            else:
                return False
    if res:
        return False
    return True