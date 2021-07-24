def solution(s):
    res = ''
    dic={
        'zero':'0',
        'one':'1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    tmp=''
    for i in s:
        if i.isdigit():
            if tmp:
                res+=dic[tmp]
                tmp=''
            res+=i
        else:
            tmp+=i
            if tmp in dic:
                res += dic[tmp]
                tmp = ''
    if tmp:
        res += dic[tmp]
    return int(res)