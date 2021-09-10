from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    res = []
    dic=defaultdict(list)
    for s in info:
        *key,value=s.split()
        for i in range(5):
            for sub in combinations(key,i):
                dic['.'.join(sub)].append(int(value))

    for key in dic.keys():
        dic[key].sort()

    for s in query:
        a,_,b,_,c,_,d,e=s.split()
        key=[]
        for i in [a,b,c,d]:
            if i !='-':
                key.append(i)
        scores = dic['.'.join(key)]
        res.append(len(scores)-bisect.bisect_left(scores,int(e)))
    return res

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))