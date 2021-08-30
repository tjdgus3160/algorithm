res=[]
def dfs(p,money,dic):
    global res
    b=int(money*0.1)
    a=money if b==0 else money-b
    res[dic[p]['idx']]+=a
    if b and dic[p]['up'] in dic:
        dfs(dic[p]['up'],b,dic)

def solution(enroll, referral, seller, amount):
    global res
    res = [0]*len(enroll)
    dic={}
    for idx,v in enumerate(enroll):
        dic[v]={'idx':idx ,'up':referral[idx]}
    for idx,v in enumerate(seller):
        dfs(v,amount[idx]*100,dic)
    return res

enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller=["young", "john", "tod", "emily", "mary"]
amount=[12, 4, 2, 5, 10]
print(solution(enroll,referral,seller,amount))