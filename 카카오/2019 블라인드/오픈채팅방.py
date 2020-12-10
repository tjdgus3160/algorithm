# hint: 최종적으로 pid당 하나의 id임으로 먼저 pid의 id를 확정시키고 로그찍기
def solution(record):
    answer = []
    pid={}
    for i in record:
        tmp=i.split()
        if tmp[0]=="Enter" or tmp[0]=="Change":
            pid.setdefault(tmp[1],"")
            pid[tmp[1]]=tmp[2]
    for i in record:
        tmp=i.split()
        if tmp[0]=="Enter":
            answer.append(pid[tmp[1]]+"님이 들어왔습니다.")
        elif tmp[0]=="Leave":
            answer.append(pid[tmp[1]]+"님이 나갔습니다.")
    return answer

arr=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(arr))

