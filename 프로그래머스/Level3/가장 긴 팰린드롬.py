def solution(s):
    n=len(s)
    res = 1
    for i in range(n-1):
        for j in range(i+1,n+1):
            cnt=j-i
            if cnt>res:
                flag=True
                for k in range((j-i)//2+1):
                    if s[i+k]!=s[j-1-k]:
                        flag=False
                        break
                if flag:
                    res=cnt
    return res

s='ababbab'
print(solution(s))