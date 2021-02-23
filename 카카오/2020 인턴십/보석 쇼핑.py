def solution(gems):
    start=0
    end=0
    res=[]
    diff=float('inf')
    last=len(gems)
    n=len(set(gems))
    dic={gems[0]:1}
    flag=1
    if len(dic) == n:
        flag = True
    while start<=end:
        if flag==n:
            if end-start<diff:
                res=[start+1,end+1]
                diff=end-start
            dic[gems[start]]-=1
            if dic[gems[start]]==0:
                flag-=1
            start+=1
        elif end+1<last:
            end+=1
            if gems[end] not in dic:
                dic[gems[end]]=1
                flag+=1
            else:
                if dic[gems[end]]==0:
                    flag+=1
                dic[gems[end]] += 1
        else:
            dic[gems[start]]-=1
            if dic[gems[start]]==0:
                flag-=1
            start+=1
    return res