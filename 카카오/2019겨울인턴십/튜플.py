import operator
def solution(s):
    tmp=[]
    dict={}
    for i in s:
        if i.isdigit():
            tmp.append(i)
        else:
            if len(tmp)>0:
                k=int("".join(tmp))
                dict.setdefault(k,0)
                dict[k]+=1
                tmp.clear()
    dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    answer=[i[0] for i in dict]
    return answer

s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))

