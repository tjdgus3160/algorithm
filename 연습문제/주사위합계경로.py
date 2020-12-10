# 주사위 합계 경로
# 주사위를 두 번 던져서 합계가 특정 수가 나오는 경우의 수와 경로 구하기
from collections import defaultdict,Counter
def find(x):
    if x<2 and x>12:
        return None
    cdict=Counter()
    ddict=defaultdict(list)

    for i in range(1,7):
        for j in range(1,7):
            t=[i,j]
            cdict[i+j]+=1
            ddict[i+j].append(t)
    return [cdict[x],ddict[x]]

print(find(5))