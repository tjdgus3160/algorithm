# 14500번
import sys
input=sys.stdin.readline

def check(x,y,block):
    global res
    cnt=0
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j]:
                cnt+=arr[i+x][j+y]
    res=max(res,cnt)

block1=[[[1,1,1,1]],[[1], [1], [1], [1]]]
block2=[[[1,1],[1,1]]]
block3=[[[1,0],[1,0],[1,1]],[[1, 1, 1], [1, 0, 0]],[[1, 1], [0, 1], [0, 1]],[[0, 0, 1], [1, 1, 1]],[[0,1],[0,1],[1,1]],[[1, 0, 0], [1, 1, 1]],[[1, 1], [1, 0], [1, 0]],[[1, 1, 1], [0, 0, 1]]]
block4=[[[1,0],[1,1],[0,1]],[[0, 1, 1], [1, 1, 0]],[[0,1],[1,1],[1,0]],[[1, 1, 0], [0, 1, 1]]]
block5=[[[1,1,1],[0,1,0]],[[0, 1], [1, 1], [0, 1]],[[0, 1, 0], [1, 1, 1]],[[1, 0], [1, 1], [1, 0]]]

n,m=map(int,input().split())
res=0
arr=[[*map(int,input().split())]for _ in range(n)]
for block in block1:
    for x in range(n-len(block)+1):
        for y in range(m-len(block[0])+1):
            check(x,y,block)

for block in block2:
    for x in range(n-len(block)+1):
        for y in range(m-len(block[0])+1):
            check(x,y,block)

for block in block3:
    for x in range(n-len(block)+1):
        for y in range(m-len(block[0])+1):
            check(x,y,block)

for block in block4:
    for x in range(n-len(block)+1):
        for y in range(m-len(block[0])+1):
            check(x,y,block)

for block in block5:
    for x in range(n - len(block)+1):
        for y in range(m - len(block[0])+1):
            check(x, y, block)
print(res)