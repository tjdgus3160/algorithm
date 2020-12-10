# BFS, 트리 깊이 고려
from collections import deque,Counter
def poss(s1,s2):
    c1=Counter(list(s1))
    c2=Counter(list(s2))
    if len(c1-c2)==1:
        return True
    return False
def solution(begin, target, words):
    answer = 0
    n=len(words)
    v={}
    dq=deque()
    for i in range(n):
        v.setdefault(words[i],False)
        if not v[words[i]] and poss(begin,words[i]):
            dq.append(words[i])
    answer+=1
    while dq:
        k=len(dq)
        while k>0:
            t=dq.popleft()
            v[t] = True
            if t==target:
                return answer
            for i in range(n):
                if not v[words[i]] and poss(t,words[i]):
                    dq.append(words[i])
            k-=1
        answer+=1
    return 0

#s1='hit'
#s2='hzt'
#print(poss(s1,s2))
b='hit'
c='wow'
arr=['hot', 'dog','dot','wow']
print(solution(b,c,arr))

# 단어에서 한 글자만 다른지 확인, zip으로 비교해서 다를경우 1
# if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
