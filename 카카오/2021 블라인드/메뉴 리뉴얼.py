import itertools

def solution(orders, course):
    answer = []
    dict = {}
    for i in orders:
        for j in course:  # 가능한 모든 조합 뽑기
            if len(i) >= j:
                l=list(itertools.combinations(i, j))
                for k in l:
                    key="".join(sorted(k))
                    dict.setdefault(key,0)
                    dict[key]+=1
    #print(sorted(dict.items(),key=lambda x:(len(x[0]),-x[1])))
    tmp=[]
    for i in sorted(dict.items(),key=lambda x:(len(x[0]),-x[1])):
        if not tmp:
            answer.append(i[0])
            tmp=[i[0],i[1]]
        else:
            if len(i[0])>len(tmp[0]) and i[1]>1:
                answer.append(i[0])
                tmp = [i[0], i[1]]
            else:
                if i[1]==tmp[1]:
                    answer.append(i[0])
    return sorted(answer)

orders=	["XYZ", "XWY", "WXA"]
course=[2,3,4]
print(solution(orders,course))