import sys
input=sys.stdin.readline

def func(tmp):
    global res
    if len(tmp)==n:
        res+=1
        return
    if len(tmp)<n:
        for i in arr:
            func(tmp+i)

arr=['1','22','333','4444']
n=int(input())
res=0
func('')
print(res)