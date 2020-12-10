def solution(s1, s2):
    a=[]
    b=[]
    for i in range(len(s1)-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            a.append(s1[i:i+2].lower())
    for i in range(len(s2)-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            b.append(s2[i:i+2].lower())
    if not a and not b:
        return 65536
    total=len(a)+len(b)
    cnt=0
    for i in a:
        if i in b:
            cnt+=1
            b.remove(i)
    return int(cnt/(total-cnt)*65536)

s1='FRANCE'
s2=''
print(solution(s1,s2))