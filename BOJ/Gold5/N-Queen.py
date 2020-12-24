# 9663번
import sys
input=sys.stdin.readline

def func(k):
    global cnt
    if k==n:
        cnt+=1
        return
    for i in range(n):
        if isused1[i] or isused2[i+k] or isused3[k-i+n-1]:
            continue
        isused1[i]=True
        isused2[k + i]=True
        isused3[k-i+n-1]=True
        func(k+1)
        isused1[i]=False
        isused2[k + i]=False
        isused3[k-i+n-1]=False

n=int(input())
cnt=0
isused1 = [False] * 40  # y(열)
isused2 = [False] * 40  # x+y(우상향 대각선)
isused3 = [False] * 40  # x-y+n-1(우하향 대각선)
func(0)
print(cnt)
