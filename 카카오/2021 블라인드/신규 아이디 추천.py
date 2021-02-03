import copy

def solution(new_id):
    tmp=[]
    prev=0
    for i in list(new_id):
        if i.isalpha():
            tmp.append(i.lower())
            prev=i
        elif i.isdigit():
            tmp.append(i)
            prev=i
        elif i in "-_.":
            if prev=='.' and i=='.':
                continue
            tmp.append(i)
            prev=i
    if tmp and tmp[0] == ".":
        del tmp[0]
    if tmp and tmp[-1] == ".":
        del tmp[-1]
    if len(tmp)==0:
        tmp.append('a')
    if len(tmp)<=2:
        while len(tmp)<3:
            tmp.append(tmp[-1])
    elif len(tmp) >= 16:
        tmp = copy.deepcopy(tmp[:15])
    if tmp and tmp[0] == ".":
        del tmp[0]
    if tmp and tmp[-1] == ".":
        del tmp[-1]
    return "".join(tmp)

new_id=	"abcdefghijklmn.p"
print(solution(new_id))
s="a"
s.isdigit()