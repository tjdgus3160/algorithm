def solution(s):
    res=''
    flag=True
    for i in s:
        if flag and i !=' ':
            if i.isalpha():
                res+=i.upper()
            else:
                res+=i
            flag=False
        elif i ==' ':
            res+=i
            flag=True
        else:
            res+=i.lower()
            flag = False
    return res