def solution(s):
    res=[0,0]
    while s != '1':
        if '0' in s:
            res[1]+=s.count('0')
            s='1'*s.count('1')
        else:
            s=bin(len(s))[2:]
            res[0]+=1
    res[0]+=1
    return res