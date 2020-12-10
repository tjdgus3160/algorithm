import itertools
# 순열
# 길이가 n인 모든 가능한 순열 구하기
def perm(s):
    if len(s)<2:
        return s
    res=[]
    for i,c in enumerate(s):
        for cc in perm(s[:i]+s[i+1:]):
            res.append(c+cc)
    return res

def perm2(s):
    res=itertools.permutations(s)
    return ["".join(i) for i in res]

# 길이가 n이하인 모든 가능한 순열 구하기
def perm3(s):
    if len(s)<2:
        return s
    res=[]
    for i,c in enumerate(s):
        res.append(c)
        for cc in perm(s[:i]+s[i+1:]):
            res.append(c+cc)
    return res

s="012"
print(perm(s))
print(perm2(s))
print(perm3(s))

# 조합
# 모든 가능한 조합 구하기 ['01', '02', '12'] 중복x
import itertools
def comb(s):
    res=itertools.combinations(s,2)
    return ["".join(i) for i in res]
s="012"

print(comb(s))

# 순열 중복허용
from itertools import product
data=['A','B','C']
result=list(product(data,repeat=2)) # 2개를 뽑는 모든 순열
print(result)

# 조합 중복 허용
from itertools import combinations_with_replacement
data=['A','B','C']
result=list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 순열
print(result)
