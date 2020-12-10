# 문자열 처리는 문자열로 리스트 쓰면 속도 훨씬 느려짐
import sys
sys.setrecursionlimit(10**9)

def check(s):
    if s[0]==')':
        return False
    cnt=0
    for i in range(len(s)):
        cnt= cnt+1 if s[i]=="(" else cnt-1
        if cnt<0:
            return False
    return True

def find(s):
    if not s:
        return ""
    u=""
    v=""
    tmp=0
    for j,i in enumerate(s):
        tmp=tmp+1 if i=="(" else tmp-1
        u+=i
        if tmp==0:
            v=s[j+1:]
            break
    if check(u):
        u+=find(v)
        return u
    a =[")" if i == "(" else "(" for i in u[1:-1]]
    tmp = "("+find(v)+")"+"".join(a)
    return tmp

def solution(p):
    if check(p):
        return p
    else:
        t=find(p)
        return str("".join(t))

p=")()()()("
print(solution(p))
