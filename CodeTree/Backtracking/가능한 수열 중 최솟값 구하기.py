import sys
input=sys.stdin.readline

def check(tmp):
    for i in range(1,len(tmp)//2+1):
        if tmp[-2*i:-i]==tmp[-i:]:
            return False
    return True

def func(k):
    if len(k)==n:
        print(k)
        exit()
    if len(k)<n:
        for i in ['4','5','6']:
            tmp=k+i
            if check(tmp):
                func(tmp)

n=int(input())
func('4')