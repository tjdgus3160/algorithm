import sys
input=sys.stdin.readline

def func(idx,cur,s,dic):
    global res
    if idx>len(s):
        res=max(res,cur)
        return
    if s[idx] in dic:
        if s[idx-1]=='+':
            func(idx + 2, cur+dic[s[idx]], s, dic)
        elif s[idx-1]=='*':
            func(idx + 2, cur*dic[s[idx]], s, dic)
        else:
            func(idx + 2, cur-dic[s[idx]], s, dic)
    else:
        for i in range(1,5):
            dic[s[idx]]=i
            if idx==0:
                func(idx + 2, i, s, dic)
            else:
                if s[idx - 1] == '+':
                    func(idx + 2, cur + dic[s[idx]], s, dic)
                elif s[idx - 1] == '*':
                    func(idx + 2, cur * dic[s[idx]], s, dic)
                else:
                    func(idx + 2, cur - dic[s[idx]], s, dic)
            del dic[s[idx]]

s=input().rstrip()
dic={}
res=0
func(0,0,s,dic)
print(res)
