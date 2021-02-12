def solution(skill, skill_trees):
    res=0
    for arr in skill_trees:
        tmp=[arr.find(i) for i in skill]
        flag=True
        for i in range(len(tmp)-1):
            if tmp[i]==-1:
                if [j for j in tmp[i+1:] if j>=0]:
                    flag=False
                    break
            elif tmp[i+1] != -1 and tmp[i]>tmp[i+1]:
                flag=False
                break
        if flag:
            res+=1
    return res