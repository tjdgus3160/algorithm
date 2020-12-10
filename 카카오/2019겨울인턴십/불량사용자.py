# hint: 명단이 같은거 중복 제거, 명부 관리해야함->set이용

import itertools
def check(s1,s2):
    res=True
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s2[i]=='*':
            continue
        if s1[i]!=s2[i]:
            return False
    return res

def solution(user_id, banned_id):
    answer = 0
    tmp=[]
    for people in list(itertools.permutations(user_id,len(banned_id))):
        flag=True
        for i in range(len(people)):
            if not check(people[i],banned_id[i]):
                flag=False
                break
        if flag and set(people) not in tmp:
            tmp.append(set(people))
            answer+=1
    return answer

user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["*rodo", "*rodo", "******"]
print(solution(user_id,banned_id))