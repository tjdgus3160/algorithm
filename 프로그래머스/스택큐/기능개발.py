# 기능개발

def solution(progresses, speeds):
    answer = []
    tmp=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            tmp.append((100-progresses[i])//speeds[i])
        else:
            tmp.append(((100-progresses[i])//speeds[i])+1)
    t=0
    cnt=1
    for i in tmp:
        if t==0:
            t=i
            continue
        if t<i:
            answer.append(cnt)
            cnt=1
            t=i
        else:
            cnt+=1
    answer.append(cnt)
    return answer

l=[95, 90, 99, 99, 80, 99]
s=	[1, 1, 1, 1, 1, 1]
print(solution(l,s))

# (p-100) => 음수, (p-100) // s => 내림한 음수(음수에서 내림은 절대값은 커짐), -((p-100)//s) => 올림한 양수
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
        print(Q)
    return [q[1] for q in Q]