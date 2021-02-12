def solution(n, words):
    dic={}
    res=[0,0]
    turn=1
    last=''
    cnt=1
    for i in words:
        if cnt>n:
            turn+=1
            cnt=1
        if last=='':
            last=i[-1]
            dic[i]=1
            cnt+=1
            continue
        if i in dic:
            return [cnt, turn]
        if last == i[0]:
            last = i[-1]
            cnt+=1
            dic[i] = 1
        else:
            return [cnt,turn]
    return res