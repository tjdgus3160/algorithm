# 9079번
import copy
from collections import deque
import sys
input=sys.stdin.readline

def check(arr):
    return len(set(sum(arr, [])))==1

def func(arr):
    cnt=0
    dq=deque([arr])
    dic={}
    dic[''.join(sum(arr, []))]=1
    while dq:
        k=len(dq)
        for _ in range(k):
            tmp=dq.popleft()
            if(check(tmp)):
                return cnt
            for i in range(3):
                tmp1 = copy.deepcopy(tmp)
                tmp2 = copy.deepcopy(tmp)
                for j in range(3):
                    tmp1[j][i]='H' if tmp1[j][i]=='T' else 'T'
                    tmp2[i][j]='H' if tmp2[i][j]=='T' else 'T'
                tmp1str=''.join(sum(tmp1, []))
                tmp2str=''.join(sum(tmp2, []))
                if tmp1str not in dic:
                    dq.append(tmp1)
                    dic[tmp1str]=1
                if tmp2str not in dic:
                    dq.append(tmp2)
                    dic[tmp2str]=1
                tmp3 = copy.deepcopy(tmp)
                for j in range(3):
                    tmp3[j][j]='H' if tmp3[j][j]=='T' else 'T'
                tmp4 = copy.deepcopy(tmp)
                for j in range(3):
                    tmp4[j][2-j]='H' if tmp4[j][2-j]=='T' else 'T'
                tmp3str=''.join(sum(tmp3, []))
                tmp4str=''.join(sum(tmp4, []))
                if tmp3str not in dic:
                    dq.append(tmp3)
                    dic[tmp3str]=1
                if tmp4str not in dic:
                    dq.append(tmp4)
                    dic[tmp4str]=1
        cnt+=1
    return -1

for _ in range(int(input())):
    arr=[]
    for _ in range(3):
        arr.append(input().split())
    print(func(arr))