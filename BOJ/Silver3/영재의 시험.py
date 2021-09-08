# 19949번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def func(k,pre1,pre2,score):
    global res
    if k==10:
        if score>=5:
            res+=1
        return
    for i in range(1,6):
        if pre1==None:
            if i==arr[k]:
                func(k+1,i,None,score+1)
            else:
                func(k+1, i, None, score)
        elif pre2==None:
            if i==arr[k]:
                func(k+1,i,pre1,score+1)
            else:
                func(k+1,i,pre1, score)
        else:
            if pre1==pre2 and pre1==i:
                continue
            if i==arr[k]:
                func(k+1,i,pre1,score+1)
            else:
                func(k+1,i,pre1, score)

arr=[*map(int,input().split())]
res=0
func(0,None,None,0)
print(res)