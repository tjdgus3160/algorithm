# hint: 카운트가 1자리 이상일수도 있는 경우 고려
def solution(s):
    n=len(s)
    answer=n
    for i in range(1,n//2+2):
        tmp=[s[j:j+i] for j in range(0,n,i)]
        cnt=1
        prev=""
        size=0
        for j in range(len(tmp)):
            if not prev:
                prev=tmp[j]
                continue
            if len(prev)!=len(tmp[j]):
                size+=len(prev)
                prev=tmp[j]
                break
            if prev:
                if prev!=tmp[j]:
                    size+=len(prev)
                    prev=tmp[j]
                    if cnt>1:
                        size+=len(str(cnt))
                    cnt=1
                else:
                    cnt+=1
        size += len(prev)
        if cnt > 1:
            size += len(str(cnt))
        answer=min(answer,size)
    return answer

s="aaaaaa"
print(solution(s))