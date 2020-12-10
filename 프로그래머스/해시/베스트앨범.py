# hint: 딕셔너리 2개 한개는 장르 뽑고 한개는 고유번호 뽑기
import operator
def solution(g, p):
    answer = []
    a = {}
    d = {}
    for i in range(len(g)):
        d.setdefault(g[i], 0)
        a.setdefault(g[i], []).append([p[i], i])
        d[g[i]] += p[i]
    d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    for i in d:
        tmp = sorted(a[i[0]],key=lambda x:(x[0],-x[1]))
        if tmp:
            answer.append(tmp.pop()[1])
        if tmp:
            answer.append(tmp.pop()[1])
    return answer

g=['classic', 'pop', 'classic', 'classic', 'pop']
p=[500,600,150,800,2500]
print(solution(g,p))
